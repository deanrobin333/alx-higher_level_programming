// 7-script.js
/* fetches the character name from this URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('#character').append(data.name);
});
