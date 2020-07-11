function user_choice(choice){
    const Http = new XMLHttpRequest();
    const url='https://localhost:5000/' + choice;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
      }
}