// Main JavaScript file for the e-commerce site

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap carousel
    const bannerCarousel = new bootstrap.Carousel(document.getElementById('bannerCarousel'), {
        interval: 5000,
        wrap: true,
        keyboard: true
    });

    // Initialize testimonial carousel
    const testimonialCarousel = new bootstrap.Carousel(document.getElementById('testimonialCarousel'), {
        interval: 6000,
        wrap: true,
        keyboard: true
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Add to cart functionality
    window.addToCart = function(productId) {
        // This is a placeholder - implement actual cart logic with AJAX
        let cartCount = parseInt(document.getElementById('cart-count').textContent);
        cartCount++;
        document.getElementById('cart-count').textContent = cartCount;
        
        // Show notification
        showNotification('Produit ajouté au panier !', 'success');
    };

    // Notification system
    function showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    // Animate statistics on scroll (removed - statistics section deleted)
    // const observerOptions = {
    //     threshold: 0.5
    // };

    // const statsObserver = new IntersectionObserver((entries) => {
    //     entries.forEach(entry => {
    //         if (entry.isIntersecting) {
    //             animateStats();
    //             statsObserver.unobserve(entry.target);
    //         }
    //     });
    // }, observerOptions);

    // const statsSection = document.querySelector('.statistics-section');
    // if (statsSection) {
    //     statsObserver.observe(statsSection);
    // }

    // function animateStats() {
    //     const statNumbers = document.querySelectorAll('.stat-item h3');
    //     statNumbers.forEach(stat => {
    //         const target = parseInt(stat.textContent);
    //         animateNumber(stat, 0, target, 2000);
    //     });
    // }

    // function animateNumber(element, start, end, duration) {
    //     const range = end - start;
    //     const increment = end > start ? 1 : -1;
    //     const stepTime = Math.abs(Math.floor(duration / range));
    //     let current = start;
        
    //     const timer = setInterval(() => {
    //         current += increment;
    //         element.textContent = current;
    //         if (current === end) {
    //             clearInterval(timer);
    //         }
    //     }, stepTime);
    // }

    // Product card hover effects
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.product-image img').style.transform = 'scale(1.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.product-image img').style.transform = 'scale(1)';
        });
    });

    // Category card hover effects
    const categoryCards = document.querySelectorAll('.category-card');
    categoryCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.category-image img').style.transform = 'scale(1.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.category-image img').style.transform = 'scale(1)';
        });
    });

    // Search functionality
    const searchForm = document.querySelector('form[action="#"]');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const searchQuery = this.querySelector('input[name="q"]').value;
            if (searchQuery.trim()) {
                // Implement search logic
                showNotification(`Recherche: ${searchQuery}`, 'info');
            }
        });
    }

    // Navbar scroll effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('shadow');
        } else {
            header.classList.remove('shadow');
        }
    });

    // Lazy loading images
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));

    // Add fade-in animation to sections
    const sections = document.querySelectorAll('section');
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, { threshold: 0.1 });

    sections.forEach(section => sectionObserver.observe(section));

    // Mobile menu close on link click
    const navLinks = document.querySelectorAll('.nav-link');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                bsCollapse.hide();
            }
        });
    });

    // Price formatting
    function formatPrice(price) {
        return new Intl.NumberFormat('fr-FR', {
            style: 'currency',
            currency: 'XOF'
        }).format(price);
    }

    // Stock availability indicator
    function updateStockIndicator(stock) {
        const stockElements = document.querySelectorAll('[data-stock]');
        stockElements.forEach(element => {
            const stockValue = parseInt(element.dataset.stock);
            if (stockValue <= 0) {
                element.innerHTML = '<span class="text-danger">Rupture de stock</span>';
            } else if (stockValue <= 5) {
                element.innerHTML = `<span class="text-warning">Stock limité (${stockValue})</span>`;
            } else {
                element.innerHTML = `<span class="text-success">En stock (${stockValue})</span>`;
            }
        });
    }

    // Initialize stock indicators
    updateStockIndicator();

    // Product quick view (placeholder)
    window.quickView = function(productId) {
        showNotification('Vue rapide du produit (ID: ' + productId + ')', 'info');
    };

    // Wishlist functionality (placeholder)
    window.addToWishlist = function(productId) {
        showNotification('Produit ajouté aux favoris !', 'success');
    };

    // Compare products (placeholder)
    window.addToCompare = function(productId) {
        showNotification('Produit ajouté à la comparaison !', 'success');
    };

    // Render star ratings
    const ratingElements = document.querySelectorAll('[data-rating]');
    ratingElements.forEach(element => {
        const rating = parseInt(element.dataset.rating);
        let starsHTML = '';
        for (let i = 0; i < rating; i++) {
            starsHTML += '<i class="fas fa-star text-warning"></i>';
        }
        for (let i = rating; i < 5; i++) {
            starsHTML += '<i class="far fa-star text-warning"></i>';
        }
        element.innerHTML = starsHTML;
    });

    console.log('E-commerce site loaded successfully!');
});
