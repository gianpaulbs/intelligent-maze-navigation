import * as UI from './constants/ui.constant.js';
import * as TYPE from './constants/type.constant.js';

let body = {
    type_maze: 0,
    type_algorithm: 0
}

const chooseTypeSize = (size) => {
    switch(size) {
        case TYPE.SHORT: 
            UI.BTN_SHORT_SIZE.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            UI.BTN_MEDIUM_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_BIG_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            break;
        case TYPE.MEDIUM:
            UI.BTN_SHORT_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_MEDIUM_SIZE.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            UI.BTN_BIG_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            break;
        case TYPE.BIG:
            UI.BTN_SHORT_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_MEDIUM_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_BIG_SIZE.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            break;
    }

    body.type_maze = size;
}

const chooseTypeAlgorithm = (algorithm) => {
    switch(algorithm) {
        case TYPE.DIJKSTRA: 
            UI.BTN_DIJKSTRA.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            UI.BTN_BFS.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_A_STAR.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            break;
        case TYPE.BFS:
            UI.BTN_DIJKSTRA.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_BFS.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            UI.BTN_A_STAR.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            break;
        case TYPE.A_STAR:
            UI.BTN_DIJKSTRA.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_BFS.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
            UI.BTN_A_STAR.style.backgroundColor = UI.BTN_SELECTED_BACKGROUND_COLOR;
            break;
    }

    body.type_algorithm = algorithm;
}

const validIfSelectedOptions = () => {
    if (body.type_maze == 0 && body.type_algorithm == 0) {
        alert('Debes escoger el tamaño del laberinto y el algoritmo de recorrido.');
        return;
    }

    if (body.type_maze == 0 && body.type_algorithm != 0) {
        alert('Debes escoger el tamaño del laberinto para generar el recorrido.');
        return;
    }
}

const send = () => {
    validIfSelectedOptions();

    axios
        .post('http://127.0.0.1:8000/generate-maze', body)
        .then((response) => {
            UI.IMAGE.src = `data:image/png;base64, ${response.data.image}`;
        })
        .catch((error) => {
            console.log(error);
        });
}

const reset = () => {
    UI.BTN_SHORT_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.BTN_MEDIUM_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.BTN_BIG_SIZE.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.BTN_DIJKSTRA.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.BTN_BFS.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.BTN_A_STAR.style.backgroundColor = UI.BTN_DEFAULT_BACKGROUND_COLOR;
    UI.IMAGE.src = 'img/laberinto.png';
    body.type_maze = 0;
    body.type_algorithm = 0;
}

UI.BTN_SHORT_SIZE.addEventListener('click', () => chooseTypeSize(1));
UI.BTN_MEDIUM_SIZE.addEventListener('click', () => chooseTypeSize(2));
UI.BTN_BIG_SIZE.addEventListener('click', () => chooseTypeSize(3));
UI.BTN_DIJKSTRA.addEventListener('click', () => chooseTypeAlgorithm(1));
UI.BTN_BFS.addEventListener('click', () => chooseTypeAlgorithm(2));
UI.BTN_A_STAR.addEventListener('click', () => chooseTypeAlgorithm(3));
UI.BTN_GENERATE_MAZE.addEventListener('click', send);
UI.BTN_RESET.addEventListener('click', reset);
