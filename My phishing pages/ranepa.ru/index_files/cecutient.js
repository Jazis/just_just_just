//ranepa.page.mainnav=Object;
function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

$().ready(function(){
if((getCookie('siteCecutient') != '0')&&(getCookie('siteCecutient') != undefined)){
	$('#page').addClass('cecutient');
	$("head").append($("<link rel='stylesheet' href='/bitrix/templates/ranepa/css/eye.css' type='text/css' media='screen' class='cecutient-css' />"));
}
if((getCookie('siteColor') != '0')&&(getCookie('siteColor') != undefined)){$('#page').addClass('color' + getCookie('siteColor'))};
if((getCookie('siteFontsize') != '0')&&(getCookie('siteFontsize') != undefined)){$('#page').addClass('fontsize-' + getCookie('siteFontsize'))};
if((getCookie('siteImages') != '0')&&(getCookie('siteImages') != undefined)){$('#page').addClass('imagesoff')};

	$('.eye').on('click',function(){
		if ($('#page').hasClass('cecutient')) {
			$('#page').removeClass('cecutient');
			$('.cecutient-css').remove();
			$('#page').removeClass('color1').removeClass('color2').removeClass('color3');
			document.cookie = "siteFontsize=0; path=/;";
			document.cookie = "siteColor=0; path=/;";
			document.cookie = "siteColor=0; path=/;";
			document.cookie = "siteCecutient=0; path=/;";
		}else{
			$('#page').addClass('cecutient');
			$("head").append($("<link rel='stylesheet' href='/bitrix/templates/ranepa/css/eye.css' type='text/css' media='screen' class='cecutient-css' />"));
			document.cookie = "siteCecutient=1; path=/;";
		};
	});
	$('.a-fontsize-small').on("click", function(){
		$('#page').addClass('fontsize-small').removeClass('fontsize-normal').removeClass('fontsize-big');
		document.cookie = "siteFontsize=small; path=/;";
	});
	$('.a-fontsize-normal').on("click", function(){
		$('#page').addClass('fontsize-normal').removeClass('fontsize-small').removeClass('fontsize-big');
		document.cookie = "siteFontsize=normal; path=/;";
	});
	$('.a-fontsize-big').on("click", function(){
		$('#page').addClass('fontsize-big').removeClass('fontsize-normal').removeClass('fontsize-small');
		document.cookie = "siteFontsize=big; path=/;";
	});
	$('.a-color1').on("click", function(){
		$('#page').addClass('color1').removeClass('color2').removeClass('color3');
		document.cookie = "siteColor=1; path=/;";
	});
	$('.a-color2').on("click", function(){
		$('#page').addClass('color2').removeClass('color1').removeClass('color3');
		document.cookie = "siteColor=2; path=/;";
	});
	$('.a-color3').on("click", function(){
		$('#page').addClass('color3').removeClass('color2').removeClass('color1');
		document.cookie = "siteColor=3; path=/;";
	});
	$('.a-imagesoff').on("click", function(){
		if($('#page').hasClass('imagesoff')){
			$('#page').removeClass('imagesoff');
			document.cookie = "siteImages=0; path=/;";
		}else{
			$('#page').addClass('imagesoff');
			document.cookie = "siteImages=1; path=/;";
		}
	});
});