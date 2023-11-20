import * as UI from './constants/ui.constant.js';
import * as TYPE from './constants/type.constant.js';

let body = {
    type_maze: 0,
    type_algorithm: 0,
    maze_structure: []
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

    body.maze_structure = [];
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

const selectedOptionsIsValid = () => {
    if (body.type_maze == 0 && body.type_algorithm == 0) {
        alert('Debes escoger el tamaño del laberinto y el algoritmo de recorrido.');
        return false;
    }

    if (body.type_maze == 0 && body.type_algorithm != 0) {
        alert('Debes escoger el tamaño del laberinto para generar el recorrido.');
        return false;
    }

    return true;
}

const send = () => {
    if (!selectedOptionsIsValid()) return;

    // const BASE_URL = 'http://127.0.0.1:8000';
    const BASE_URL = 'https://intelligent-maze-navigation-9ef60ddb10a3.herokuapp.com'
    axios
        .post(`${BASE_URL}/generate-maze`, body)
        .then((response) => {
            UI.IMAGE.src = `data:image/png;base64, ${response.data.image}`;
            UI.TIME_CONTAINER.style.display = 'block';
            UI.TIME_LABEL.innerText = `${response.data.time} s`;
            body.maze_structure = response.data.maze_structure;
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
    UI.TIME_CONTAINER.style.display = 'none';
    body.type_maze = 0;
    body.type_algorithm = 0;
}

UI.BTN_SHORT_SIZE.addEventListener('click', () => chooseTypeSize(1));
UI.BTN_MEDIUM_SIZE.addEventListener('click', () => chooseTypeSize(2));
UI.BTN_BIG_SIZE.addEventListener('click', () => chooseTypeSize(3));
UI.BTN_DIJKSTRA.addEventListener('click', () => chooseTypeAlgorithm(1));
UI.BTN_BFS.addEventListener('click', () => chooseTypeAlgorithm(2));
UI.BTN_A_STAR.addEventListener('click', () => chooseTypeAlgorithm(3));
UI.BTN_GENERATE_MAZE.addEventListener('click', (event) =>  {
    event.preventDefault();
    send();
});
UI.BTN_RESET.addEventListener('click', reset);
