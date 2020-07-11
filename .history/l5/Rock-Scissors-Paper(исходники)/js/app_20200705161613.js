function user_choicee(choice){
    const Http = new XMLHttpRequest();
    const url='https://localhost:5000/' + choise;
    Http.open("GET", url);
    Http.send();
}