//ranepa.page.mainnav=Object;
$().ready(function(){
	$('.mobilemenu_button').on('click',function(){
		$('#mobilemenu').removeClass('close');
		$('html').addClass('mm-opening');
	});
	$('#login').on('click',function(){
		$('#login .bx-system-auth-form').addClass('open');
		$('html').addClass('mm-opening');
	});
	$('#map-plan').on('click',function(){
		$('.map').addClass('open');
		$('html').addClass('mm-opening');
	});
	$('#plan-univer').on('click',function(){
		$('.plan-univer').addClass('open');
		$('html').addClass('mm-opening');
	});
	$('.mobilemenu_back').on('click',function(){
		$('html').removeClass('mm-opening');
		$('#mobilemenu').addClass('close');
		$('#login .bx-system-auth-form, .map, .plan-univer').removeClass('open');
	});
	$('li .mm-next').on('click',function(){
		$('#mm-0').addClass('mm-subopened');
		$('#mm-0').removeClass('mm-current');
		$('.mm-highest').addClass('mm-hidden');
		$('.mm-highest').removeClass('mm-highest');
		$(this.getAttribute('data-target')).addClass('mm-highest');
		$(this.getAttribute('data-target')).removeClass('mm-hidden');
	});
	$('.item124').hover(
		function(){
			$('.dark').addClass('active');
		},
		function(){
			$('.dark').removeClass('active');
		}
	);
	$('#totop-scroller, .anchor').click( function(){
		var scroll_el = $(this).attr('href');
		console.log($(this));
	    if ($(scroll_el).length != 0) {
		    $('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 500);
	    }
		return false;
    });
});