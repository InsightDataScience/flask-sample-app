$(document).ready(function() {
    $('#btn-hide-text').click(function() { $('#additional_text').hide() } );
    $('#btn-show-text').click(function() { $('#additional_text').show() } );
    $('#btn-show-route').click(function() {
      var userName = $('#user_name').val(),
          uri = "/user/" + userName;
      $.get(uri, function(data, status) {
        console.log('Printing on browser: ' + JSON.stringify(data));
      });
    });
});
