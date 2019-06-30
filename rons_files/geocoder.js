$(document).ready(function () {
  $("#btnGeocode").click(function () {

    app_id = "p1ZbPLm8Z8ASYJtL1pCe";
    app_code = "bb2z_o2W3dNF6tY_3ysqpQ";
    restapi = "https://geocoder.cit.api.here.com/6.2/geocode.json";
		
    searchquery = '425 W Randolph Chicago';

    $.ajax({
      url: restapi,
      type: 'GET',
      dataType: 'jsonp',
      jsonp: 'jsoncallback',
      data: {
        searchtext: searchquery,
        app_id: app_id,
        app_code: app_code,
        gen: '8'
      },
      success: function (data) {
        $("#divResult").text(data.Response.View[0].Result[0].Location.DisplayPosition.Latitude + ' ' + data.Response.View[0].Result[0].Location.DisplayPosition.Longitude);
      }
    });
  });
});