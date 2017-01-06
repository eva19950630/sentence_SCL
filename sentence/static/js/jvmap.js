jQuery(document).ready(function () {
    jQuery('#vmap').vectorMap({
        map: 'world_en'
        , onRegionClick: function (element, code, region) {
             country_code = code.toUpperCase();
            $.get('/getcountry/', {
                country_UpperCode : country_code
                   
             ,}, function (data) {
                country = JSON.parse(data);
                console.log(country.country);
                var message = 'You clicked "' + country.country + '" which has the code: ' + code.toUpperCase();
                alert(message);
            });
            
            
           
        }
    });
});