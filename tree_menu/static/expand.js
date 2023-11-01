document.addEventListener('DOMContentLoaded', function() {
    var expandables = document.querySelectorAll('.expandable');
    expandables.forEach((expandable) => {
        var toggle = expandable.querySelector('.toggle');
        var has_children = expandable.querySelector('.children') != null;
        if (expandable.classList.contains('expanded') && has_children) {
            toggle.textContent = '-';
        }
        toggle.addEventListener('click', function(event) {
            event.preventDefault();
            if (has_children == false) {
                return;
            }
            expandable.classList.toggle('expanded');
            toggle.textContent = expandable.classList.contains('expanded') ? '-' : '+';
        });
    });
});
