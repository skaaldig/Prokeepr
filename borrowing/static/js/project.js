/* Project specific Javascript goes here. */
$(document).ready( () => {
  $('.data__row').on('click', event => {
    $(event.currentTarget).next().toggle();
  })
})
