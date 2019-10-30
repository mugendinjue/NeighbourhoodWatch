$(document).ready(function(){
  $('#createN').click(function(){
    $('#neighbourhood').fadeIn('slow');
  })
  $('.close').click(function(){
    $('#neighbourhood').fadeOut('slow');
  })
  $('.submit').click(function(){
    $('#neighbourhood').fadeOut('slow');
  })
  var user_id = $(this).find($('.get_user_id'))
  $('form#the_hood').submit(function(e){
    e.preventDefault()
    hood_form = $('form#the_hood')

    $.ajax({
      'url':'/new/neighbourhood/'+user_id.val()+'',
      'type':'POST',
      'data':hood_form.serialize(),
      'dataType':'json',
      'success':function(data){
        console.log(data['success'])
      }
    })
    $('#id_neighbourhood_name').val('')
    $('#id_neighbourhood_location').val('') 
  })
})

