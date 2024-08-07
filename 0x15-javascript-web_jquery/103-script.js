// 103-script.js
// fetches and prints how to say “Hello” depending on the language
/* Original link was - https://www.fourtonfish.com/hellosalut/hello/
 * but has since changed to https://hellosalut.stefanbohacek.dev/
 */
$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
