$('#toggle_header').on('click', function () {
  if ($('header').hasClass('red')) { $(this).toggleClass('green'); } else { $(this).toggleClass('red'); }
});
