function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$(document).ready(function(){
	$('.languages li').click(function(event){
           // event.preventDefault();
			var url =$('.name_trans').val()
			var language=($(this).text());
			switch(language){
					case 'Հայ': language='hy';break;
					case 'En':  language='en';break;
					case 'Рус':  language='ru';break;
			}
			$.ajax({
                    url:'ajax/',
					type:"POST",
					data:{'lang':language},
					success:function(e){
							alert(e)
           }
		
     })
  })	

})
