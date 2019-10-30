console.log("ready")
$(document).ready(function () {
  $('#hood_health').click(function () {
    $('#health_form').slideToggle('slow')
  })
  $('#hood_security').click(function () {
    $('#security_form').slideToggle('slow')
  })
  $('#on_submit').click(function () {
    $('#security_form').slideToggle('slow')
  })
  $('#af_submit').click(function () {
    $('#health_form').slideToggle('slow')
  })

  // the post modal
  $('#post').click(function(){
    $('#user_post').fadeIn('slow');
    console.log('sdfdf')
  })
  $('.close').click(function(){
    $('#user_post').fadeOut('slow');
  })
  $('#submit').click(function(){
    $('#user_post').fadeOut('slow');
  })

// toogle the contacts section
  $('#showmore').click(function(){
    $('#more').slideToggle('slow')
  })
  $('#showS').click(function(){
    $('#showD').slideToggle('slow')
  })

  // health submit form

  var hood_id = $(this).find($('.myhood'))
  var user_id = $(this).find($('.currentuser'))

  $('form#form_health').submit(function (e) {
    e.preventDefault()
    health_data = $('form#form_health')
    $.ajax({
      'url': '/new/health/' + hood_id.val() + '',
      'type': 'POST',
      'data': health_data.serialize(),
      'dataType': 'json',
      'success': function (data) {
        console.log(data['success'])
      }
    })
  })

  // security submit form

  $('form#form_security').submit(function (e) {
    e.preventDefault()
    security_data = $('form#form_security')
    $.ajax({
      'url': '/new/security/' + hood_id.val() + '',
      'type': 'POST',
      'data': security_data.serialize(),
      'dataType': 'json',
      'success': function (data) {
        console.log(data['success'])
      }
    })
  })

  // the post submit form

  $('form#postForm').submit(function (e) {
    e.preventDefault()
    post_data = $('form#postForm')
    $.ajax({
      'url': '/new/post/' + hood_id.val() + '/'+ user_id.val() +'',
      'type': 'POST',
      'data': post_data.serialize(),
      'dataType': 'json',
      'success': function (data) {
        console.log(data['success'])
      }
    })
  })


})