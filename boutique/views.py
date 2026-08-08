from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Banner, Categorie, Produit, Promotion, Avantage, Temoignage, Contact, PanierItem, Commande, CommandeItem, Favori
from .forms import TemoignageForm, ContactForm


def home(request):
    # Récupérer les bannières actives
    banners = Banner.objects.filter(active=True)
    
    # Récupérer les catégories actives
    categories = Categorie.objects.filter(active=True)
    
    # Récupérer les nouveaux produits (8 derniers)
    nouveaux_produits = Produit.objects.filter(est_nouveau=True, stock__gt=0)[:8]
    
    # Récupérer les promotions actives
    from django.utils import timezone
    promotions = Promotion.objects.filter(
        active=True,
        date_debut__lte=timezone.now(),
        date_fin__gte=timezone.now()
    ).first()
    
    # Récupérer les avantages
    avantages = Avantage.objects.all()
    
    # Récupérer les témoignages actifs
    temoignages = Temoignage.objects.filter(active=True)
    
    # Récupérer les informations de contact
    contact = Contact.objects.first()
    
    # Gestion du formulaire de témoignage
    temoignage_form = None
    if request.method == 'POST' and 'ajouter_temoignage' in request.POST:
        temoignage_form = TemoignageForm(request.POST, request.FILES)
        if temoignage_form.is_valid():
            temoignage = temoignage_form.save(commit=False)
            temoignage.active = True  # Les témoignages s'affichent immédiatement
            temoignage.save()
            messages.success(request, 'Merci pour votre témoignage ! Il est maintenant visible.')
            temoignage_form = TemoignageForm()  # Reset form
    else:
        temoignage_form = TemoignageForm()
    
    # Calculer les statistiques réelles
    from django.utils import timezone
    stats = {
        'nb_produits': Produit.objects.count(),
        'nb_categories': Categorie.objects.count(),
        'nb_produits_stock': Produit.objects.filter(stock__gt=0).count(),
        'nb_produits_populaires': Produit.objects.filter(est_populaire=True).count(),
        'nb_promotions': Promotion.objects.filter(
            active=True,
            date_debut__lte=timezone.now(),
            date_fin__gte=timezone.now()
        ).count(),
        'nb_temoignages': Temoignage.objects.filter(active=True).count(),
        'nb_commandes': 0,  # À implémenter avec un modèle Commande
        'nb_clients': 0,  # À implémenter avec un modèle Client
    }
    
    context = {
        'banners': banners,
        'categories': categories,
        'nouveaux_produits': nouveaux_produits,
        'promotion': promotions,
        'avantages': avantages,
        'temoignages': temoignages,
        'contact': contact,
        'stats': stats,
        'temoignage_form': temoignage_form,
    }
    
    return render(request, 'boutique/accueil.html', context)


def boutique(request):
    # Récupérer les catégories actives pour les filtres
    categories = Categorie.objects.filter(active=True)
    
    # Récupérer les informations de contact
    contact = Contact.objects.first()
    
    # Base queryset pour les produits
    produits = Produit.objects.all()
    
    # Recherche
    search_query = request.GET.get('search', '')
    if search_query:
        produits = produits.filter(
            Q(nom__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Filtrage par catégorie
    category_id = request.GET.get('category', '')
    if category_id:
        produits = produits.filter(categorie_id=category_id)
    
    # Filtrage par disponibilité
    availability = request.GET.get('availability', '')
    if availability == 'in_stock':
        produits = produits.filter(stock__gt=0)
    elif availability == 'out_of_stock':
        produits = produits.filter(stock=0)
    
    # Tri des produits
    sort_by = request.GET.get('sort', '')
    if sort_by == 'newest':
        produits = produits.order_by('-date_creation')
    elif sort_by == 'popular':
        produits = produits.filter(est_populaire=True)
    elif sort_by == 'price_asc':
        produits = produits.order_by('prix')
    elif sort_by == 'price_desc':
        produits = produits.order_by('-prix')
    else:
        produits = produits.order_by('-date_creation')
    
    # Pagination (12 produits par page)
    paginator = Paginator(produits, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'contact': contact,
        'page_obj': page_obj,
        'search_query': search_query,
        'category_id': category_id,
        'availability': availability,
        'sort_by': sort_by,
    }
    
    return render(request, 'boutique/boutique.html', context)


def contact(request):
    # Récupérer les informations de contact
    contact_info = Contact.objects.first()
    
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            nom = contact_form.cleaned_data['nom']
            email = contact_form.cleaned_data['email']
            sujet = contact_form.cleaned_data['sujet']
            message = contact_form.cleaned_data['message']
            
            # Envoyer l'email
            try:
                send_mail(
                    f'Contact de {nom} - {sujet}',
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'contact@mounishop.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Votre message a été envoyé avec succès ! Nous vous répondrons bientôt.')
                contact_form = ContactForm()
            except Exception as e:
                messages.error(request, 'Une erreur est survenue lors de l\'envoi du message. Veuillez réessayer.')
    
    context = {
        'contact': contact_info,
        'contact_form': contact_form,
    }
    
    return render(request, 'boutique/contact.html', context)


def detail_produit(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    produits_similaires = Produit.objects.filter(categorie=produit.categorie).exclude(pk=produit.pk)[:4]
    contact = Contact.objects.first()

    product_images = [produit.image.url] * 4 if produit.image else []

    context = {
        'produit': produit,
        'product_images': product_images,
        'produits_similaires': produits_similaires,
        'contact': contact,
        'product_url': request.build_absolute_uri(),
    }

    return render(request, 'boutique/detail_produit.html', context)


def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    
    if produit.stock <= 0:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Ce produit est en rupture de stock.'
            })
        messages.warning(request, 'Ce produit est en rupture de stock.')
        return redirect('boutique')
    
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    # Si l'utilisateur est connecté, lier le panier à l'utilisateur
    if request.user.is_authenticated:
        panier_item, created = PanierItem.objects.get_or_create(
            utilisateur=request.user,
            produit=produit,
            defaults={'quantite': 1, 'session_key': session_key}
        )
        # Compter les items du panier pour l'utilisateur connecté
        cart_count = PanierItem.objects.filter(utilisateur=request.user).count()
    else:
        panier_item, created = PanierItem.objects.get_or_create(
            session_key=session_key,
            produit=produit,
            defaults={'quantite': 1}
        )
        # Compter les items du panier pour l'utilisateur non connecté
        cart_count = PanierItem.objects.filter(session_key=session_key).count()
    
    if not created:
        panier_item.quantite += 1
        panier_item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'{produit.nom} ajouté au panier',
            'cart_count': cart_count
        })
    
    messages.success(request, f'{produit.nom} ajouté au panier')
    return redirect('boutique')


def panier(request):
    session_key = request.session.session_key
    
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    # Si l'utilisateur est connecté, récupérer son panier
    if request.user.is_authenticated:
        panier_items = PanierItem.objects.filter(utilisateur=request.user)
    else:
        panier_items = PanierItem.objects.filter(session_key=session_key)
    
    total_general = sum(item.total for item in panier_items)
    
    context = {
        'panier_items': panier_items,
        'total_general': total_general,
    }
    
    return render(request, 'boutique/panier.html', context)


def modifier_quantite(request, item_id):
    panier_item = get_object_or_404(PanierItem, id=item_id)
    
    # Vérifier que l'utilisateur a le droit de modifier cet item
    if request.user.is_authenticated:
        if panier_item.utilisateur != request.user:
            messages.error(request, 'Accès refusé')
            return redirect('panier')
    else:
        if panier_item.session_key != request.session.session_key:
            messages.error(request, 'Accès refusé')
            return redirect('panier')
    
    nouvelle_quantite = int(request.POST.get('quantite', 1))
    
    if nouvelle_quantite > 0:
        panier_item.quantite = nouvelle_quantite
        panier_item.save()
    else:
        panier_item.delete()
    
    return redirect('panier')


def supprimer_du_panier(request, item_id):
    panier_item = get_object_or_404(PanierItem, id=item_id)
    
    # Vérifier que l'utilisateur a le droit de supprimer cet item
    if request.user.is_authenticated:
        if panier_item.utilisateur != request.user:
            messages.error(request, 'Accès refusé')
            return redirect('panier')
    else:
        if panier_item.session_key != request.session.session_key:
            messages.error(request, 'Accès refusé')
            return redirect('panier')
    
    panier_item.delete()
    messages.success(request, 'Produit supprimé du panier')
    
    return redirect('panier')


def commande(request, produit_id=None):
    session_key = request.session.session_key
    
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    # Si un produit_id est fourni, l'ajouter au panier
    if produit_id:
        produit = get_object_or_404(Produit, id=produit_id)
        if produit.stock > 0:
            if request.user.is_authenticated:
                PanierItem.objects.get_or_create(
                    utilisateur=request.user,
                    produit=produit,
                    defaults={'quantite': 1, 'session_key': session_key}
                )
            else:
                PanierItem.objects.get_or_create(
                    session_key=session_key,
                    produit=produit,
                    defaults={'quantite': 1}
                )
    
    # Récupérer les items du panier
    if request.user.is_authenticated:
        panier_items = PanierItem.objects.filter(utilisateur=request.user)
    else:
        panier_items = PanierItem.objects.filter(session_key=session_key)
    
    total_general = sum(item.total for item in panier_items)
    
    if not panier_items:
        return redirect('panier')
    
    if request.method == 'POST':
        # Créer la commande
        commande = Commande.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email', ''),
            telephone=request.POST.get('telephone'),
            adresse=request.POST.get('adresse'),
            ville=request.POST.get('ville'),
            pays=request.POST.get('pays', "Côte d'Ivoire"),
            mode_paiement=request.POST.get('paiement', 'especes'),
            notes=request.POST.get('notes', ''),
            total=total_general,
            session_key=session_key
        )
        
        # Créer les articles de commande
        for item in panier_items:
            CommandeItem.objects.create(
                commande=commande,
                produit=item.produit,
                quantite=item.quantite,
                prix=item.produit.prix
            )
        
        # Vider le panier
        panier_items.delete()
        
        # Envoyer un email de notification pour la nouvelle commande
        try:
            from django.core.mail import send_mail
            from django.conf import settings
            
            # Construire le message de commande
            message_commande = f'''Nouvelle commande reçue sur Univers des Pierres

Informations client :
- Nom : {commande.nom}
- Téléphone : {commande.telephone}
- Ville : {commande.ville}
- Pays : {commande.pays}
- Adresse : {commande.adresse}
- Mode de paiement : {commande.get_mode_paiement_display()}

Détails de la commande :
'''
            
            for item in commande.items.all():
                message_commande += f"- {item.produit.nom} x {item.quantite} = {item.total} FCFA\n"
            
            message_commande += f'\nTotal : {commande.total} FCFA'
            
            if commande.notes:
                message_commande += f'\n\nNotes : {commande.notes}'
            
            send_mail(
                f'Nouvelle commande #{commande.id} - {commande.nom}',
                message_commande,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            # En cas d'erreur d'envoi d'email, on continue quand même
            print(f"Erreur lors de l'envoi de l'email: {e}")
        
        messages.success(request, 'Votre commande a été enregistrée avec succès ! Nous vous contacterons bientôt.')
        return redirect('home')
    
    context = {
        'panier_items': panier_items,
        'total_general': total_general,
    }
    
    return render(request, 'boutique/commande.html', context)


def recherche(request):
    query = request.GET.get('q', '')
    
    if query:
        produits = Produit.objects.filter(
            Q(nom__icontains=query) | 
            Q(description__icontains=query) |
            Q(categorie__nom__icontains=query)
        ).distinct()
    else:
        produits = Produit.objects.none()
    
    # Pagination
    paginator = Paginator(produits, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'total_results': produits.count(),
    }
    
    return render(request, 'boutique/recherche.html', context)


@login_required
def ajouter_favori(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    favori, created = Favori.objects.get_or_create(
        utilisateur=request.user,
        produit=produit
    )
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if created:
            return JsonResponse({
                'success': True,
                'message': f'{produit.nom} ajouté aux favoris',
                'favorites_count': Favori.objects.filter(utilisateur=request.user).count()
            })
        else:
            return JsonResponse({
                'success': True,
                'message': f'{produit.nom} est déjà dans vos favoris',
                'favorites_count': Favori.objects.filter(utilisateur=request.user).count()
            })
    
    if created:
        messages.success(request, f'{produit.nom} ajouté aux favoris')
    else:
        messages.info(request, f'{produit.nom} est déjà dans vos favoris')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def supprimer_favori(request, favori_id):
    favori = get_object_or_404(Favori, id=favori_id, utilisateur=request.user)
    produit_nom = favori.produit.nom
    favori.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': f'{produit_nom} retiré des favoris',
            'favorites_count': Favori.objects.filter(utilisateur=request.user).count()
        })
    
    messages.success(request, f'{produit_nom} retiré des favoris')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def favoris(request):
    favoris = Favori.objects.filter(utilisateur=request.user).select_related('produit')
    
    context = {
        'favoris': favoris,
    }
    
    return render(request, 'boutique/favoris.html', context)


@login_required
def admin_commandes(request):
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Accès refusé. Vous n\'avez pas les permissions nécessaires.')
        return redirect('home')
    
    commandes = Commande.objects.all().order_by('-date_creation')
    
    # Filtrage par statut
    statut_filter = request.GET.get('statut')
    if statut_filter:
        commandes = commandes.filter(statut=statut_filter)
    
    # Pagination
    paginator = Paginator(commandes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'statut_filter': statut_filter,
    }
    
    return render(request, 'boutique/admin_commandes.html', context)


@login_required
def admin_commande_detail(request, commande_id):
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Accès refusé. Vous n\'avez pas les permissions nécessaires.')
        return redirect('home')
    
    commande = get_object_or_404(Commande, id=commande_id)
    
    if request.method == 'POST':
        nouveau_statut = request.POST.get('statut')
        if nouveau_statut in ['en_attente', 'confirmee', 'en_cours', 'livree', 'annulee']:
            commande.statut = nouveau_statut
            commande.save()
            message = f'''Une nouvelle commande a été passée sur Univers des Pierres.

Détails de la commande: mis à jour'''
        return redirect('admin_commande_detail', commande_id=commande_id)
    
    context = {
        'commande': commande,
    }
    
    return render(request, 'boutique/admin_commande_detail.html', context)
