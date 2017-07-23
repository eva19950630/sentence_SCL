function readURL2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var imagePreviewid = $('#imagePreview');
            imagePreviewid.css('background-image', 'url('+e.target.result +')');
            imagePreviewid.hide();
            imagePreviewid.fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("input[name='upuserpic']").on("change",function() {
    readURL2(this);
});