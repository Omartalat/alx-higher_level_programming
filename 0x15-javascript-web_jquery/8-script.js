$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
    const movies = []
    for (const property in data) {
        if (property === title) {
            list.push(data[property])
        }
    }
    for (let i = 0; i < movies; i++) {
        $('UL#list_movies').add(`<li>${movies[i]}</li>`)
    }
});