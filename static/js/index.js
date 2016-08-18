  $(function() {
    $('#calculate').bind('click', function() {
      $.getJSON('/_submit', {
        n1: $('input[name="n1"]').val(),
        n2: $('input[name="n2"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });
