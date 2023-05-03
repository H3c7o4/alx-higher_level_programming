$('#toggle_header').on('click', function () {
  if ($(this).hasClass('red')) { $(this).toggleClass('green'); } else { $(this).toggleClass('red'); }
});
