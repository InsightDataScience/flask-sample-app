$(function() {
    $('#btn-hide-text').click(function() { $('#additional_text').hide() } );
    $('#btn-show-text').click(function() { $('#additional_text').show() } );
    $('#btn-show-route').click(function() {
      $.get("user/super_user", function(data, status) {
        console.log('blah' + JSON.stringify(data));
      });
    });
});
