document.addEventListener('DOMContentLoaded', function() {
    var expandables = document.querySelectorAll('.expandable');
    expandables.forEach(function(expandable) {
        expandable.addEventListener('click', function(event) {
            var children = this.querySelector('.children');
            if (children != null) {
                children.style.display = children.style.display == 'none' ? 'block' : 'none';
            }
            event.stopPropagation();
            event.preventDefault();
        });
    });
});