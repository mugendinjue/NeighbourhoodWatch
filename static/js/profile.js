$(document).ready(function(){
  console.log("profile")
  $('#createB').click(function(){
    $('#biz').fadeIn('slow');
  })
  $('.close').click(function(){
    $('#biz').fadeOut('slow');
  })
  $('.submit').click(function(){
    $('#biz').fadeOut('slow');
  })
  var user_id = $(this).find($('.get_user_id'))
  $('form#the_biz').submit(function(e){
    e.preventDefault()
    biz_form = $('form#the_biz')
    $.ajax({
      'url':'/new/business/'+user_id.val()+'',
      'type':'POST',
      'data':biz_form.serialize(),
      'dataType':'json',
      'success':function(data){
        console.log(data['success'])
      }
    })
    $('#id_name').val('')
    $('#id_business_email').val('') 
  })
  $('#addOccupant').click(function(){
    $('#occupants').fadeIn('slow');
  })
  $('.close').click(function(){
    $('#occupants').fadeOut('slow');
  })
  // var user_id = $(this).find($('.get_user_id'))
  // $('form#the_biz').submit(function(e){
  //   e.preventDefault()
  //   biz_form = $('form#the_biz')

  //   $.ajax({
  //     'url':'/new/business/'+user_id.val()+'',
  //     'type':'POST',
  //     'data':biz_form.serialize(),
  //     'dataType':'json',
  //     'success':function(data){
  //       console.log(data['success'])
  //     }
  //   })
  //   $('#id_name').val('')
  //   $('#id_business_email').val('') 
  // })
})