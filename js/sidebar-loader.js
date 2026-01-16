document.addEventListener("DOMContentLoaded", function () {
    fetch('sidebar-content.html?v=' + Date.now())
        .then(response => response.text())
        .then(data => {
            // Find the container for the sidebar
            // In the original file, it's .deznav-scroll containing the ul#menu
            const sidebarScrollContainer = document.querySelector('.deznav-scroll');

            if (sidebarScrollContainer) {
                // Replace content with the loaded HTML
                sidebarScrollContainer.innerHTML = data;

                // Inject FontAwesome for sidebar icons
                if (!document.getElementById('font-awesome-css')) {
                    const link = document.createElement('link');
                    link.id = 'font-awesome-css';
                    link.rel = 'stylesheet';
                    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css';
                    document.head.appendChild(link);
                }

                // Force triggering a resize event so that the main template script (custom.min.js) 
                // recalculates the sidebar and content height.
                setTimeout(() => {
                    window.dispatchEvent(new Event('resize'));
                }, 100);

                // --- Highlight Active Link Logic ---
                const currentPath = window.location.pathname;
                const pageName = currentPath.split("/").pop() || 'index.html'; // Default to index.html if empty

                // Find the link that matches the current page
                const links = sidebarScrollContainer.querySelectorAll('a');

                links.forEach(link => {
                    const href = link.getAttribute('href');
                    if (href === pageName) {
                        // Add active class to the link and its parent list item
                        link.classList.add('mm-active');
                        link.parentElement.classList.add('mm-active');

                        // If it's a submenu (not the case in current flat list, but good for future)
                        // This logic handles nested menus common in metisMenu
                        let parent = link.parentElement.parentElement;
                        while (parent && parent.tagName === 'UL' && !parent.classList.contains('metismenu')) {
                            parent.classList.add('mm-show');
                            parent.parentElement.classList.add('mm-active');
                            parent = parent.parentElement.parentElement;
                        }
                    }
                });

                // --- Re-initialize Plugins ---
                // MetisMenu needs to be initialized on the new #menu element
                if (typeof jQuery !== 'undefined' && jQuery.fn.metisMenu) {
                    jQuery('#menu').metisMenu();
                }
            }
        })
        .catch(error => console.error('Error loading sidebar:', error));
});
