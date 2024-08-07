// 102-script.js
// fetches and prints how to say “Hello” depending on the language
/* Original link was - https://www.fourtonfish.com/hellosalut/hello/
 * but has since changed to https://hellosalut.stefanbohacek.dev/
 */
$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
