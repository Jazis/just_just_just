function addScript(src)
{
	var newJS = document.createElement("script");
	newJS.type = "text/javascript";
	newJS.src =  src;
	document.getElementsByTagName("head")[0].appendChild(newJS);
}
var path = location.origin ? location.origin : location.href.replace(location.pathname,'');
//Set global constant
window.ranepa = Object;
ranepa.page = Object;
addScript(path + "/bitrix/templates/ranepa/js/domelement.append.patch.js");
addScript(path + "/bitrix/templates/ranepa/js/domelement.after.patch.js");
addScript(path + "/bitrix/templates/ranepa/js/domelement.closest.patch.js");
addScript(path + "/bitrix/templates/ranepa/plugins/html5shiv.js");
addScript(path + "/bitrix/templates/ranepa/plugins/jquery/jquery.mobile.custom.min.js");
addScript(path + "/bitrix/templates/ranepa/js/mainnav.js");
addScript(path + "/bitrix/templates/ranepa/js/cecutient.js");