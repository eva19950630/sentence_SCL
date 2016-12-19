function onSignIn(googleUser) {
    console.log("login");
    // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile();
    $('#user-name').html(profile.getName());
    $('#user-pic').replaceWith('<img src="' + profile.getImageUrl() + '" height="40" width="40">');
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());
    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);
    //gapi.auth2.init(true);
    //    var xhr = new XMLHttpRequest();
    //    xhr.open('POST', 'https://yourbackend.example.com/tokensignin');
    //    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    //    xhr.onload = function () {
    //        console.log('Signed in as: ' + xhr.responseText);
    //    };
    //    xhr.send('idtoken=' + id_token);
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}
//python manage.py runserver localhost:8000
var googleUser = {};
var startApp = function () {
    gapi.load('auth2', function () {
        // Retrieve the singleton for the GoogleAuth library and set up the client.
        auth2 = gapi.auth2.init({
            client_id: '17252888188-om3sbh9djgv8gk720e7gl5tcrjj2r6hn.apps.googleusercontent.com'
            , cookiepolicy: 'single_host_origin', // Request scopes in addition to 'profile' and 'email'
            //scope: 'additional_scope'
        });
        attachSignin(document.getElementById('customBtn-login'));
        attachSignin(document.getElementById('customBtn-signup'));
    });
};

function attachSignin(element) {
    //console.log(element.id);
    auth2.attachClickHandler(element, {}, function (googleUser) {
        var profile = googleUser.getBasicProfile();
        $('#user-name').html(profile.getName());
        $('#user-pic').replaceWith('<img src="' + profile.getImageUrl() + '" height="40" width="40">');
        //        document.getElementById('name').innerText = "Signed in: " + googleUser.getBasicProfile().getName();
    }, function (error) {
        alert(JSON.stringify(error, undefined, 2));
    });
}