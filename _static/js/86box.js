/* Toggle containers, modified from: https://stackoverflow.com/questions/2454577/sphinx-restructuredtext-show-hide-code-snippets */
$(document).ready(function() {
	/* Hide all toggle containers. */
	$('.toggle').children().not('.toggle-header').hide();
	$('.toggle').toggleClass('toggle-closed');

	/* Add click handlers for the header. */
	$('.toggle-header').click(function() {
		/* Toggle the container. */
		$(this).parent().children().not('.toggle-header').toggle(400);
    	$(this).parent().toggleClass('toggle-open toggle-closed');
	});

	/* Fix scroll position if a heading is provided in the URL.
	   Actually hit or miss but I can't think of a better solution. */
	if ($('.toggle').length && document.location.hash) {
		$(window).on('load', function() {
			setTimeout(function() {
				var hash = document.location.hash;
				document.location.hash = hash + '_';
				document.location.hash = hash;
			}, 0);
		});
	}
});
