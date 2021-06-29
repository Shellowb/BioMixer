const is_clicked = {value : false}

function makeVisible(id){
    let element = document.getElementById(id);
    if (is_clicked.value) {
        element.style.display = 'none';
        element.style.visibility = 'hidden';
        is_clicked.value = false;
    }
    else {
        element.style.display = 'inline';
        element.style.visibility = 'visible';
        is_clicked.value = true;
    }

}

function getElementsValuesFromParent(id){
    let parent = document.getElementById(id);
    let children = parent.getElementsByTagName("input");
    let n_children = children.length;
    let values = []
    for(let i=0; i < n_children; i++){
        values.push(children[i].value);
    }
    return values;
}

function validateValue(value){
    let is_valid = false;
    if ((typeof value) == "string"){
        is_valid = is_valid && (0 < value.length);
        is_valid = is_valid && value.length < 3;
    }
    if ((typeof value == "number")){
        is_valid = is_valid || (value > 0);
    }
    return is_valid
}

function validateInputs(id) {
    const values = getElementsValuesFromParent(id);
    let is_valid = false;
    for (let i = 0; i < values.length; i++){
        is_valid = validateValue(values[i]);
        console.log(is_valid, "type ", typeof values[i],values[i])
    }
    let mix_is_valid = is_valid ? "Your mix is valid" : "Your mix is Not valid";
    document.getElementById('validate').innerHTML = mix_is_valid;
    document.getElementById('validate').style.display = 'inline';
    if (!is_valid) {
        document.getElementById('send').disabled = true;
    }
}

const start_stop_classes = 
    {   active: 'btn-fab-green', active_text: 'Start', 
        inactive: 'btn-danger', inactive_text: 'Stop'}

const progressbar_classes ={
    states : ['inactive', 'current', 'active'],
    materials : {
        "m1" : 0,
        "m2" : 0,
        "m3" : 0,
        "m4" : 0,
        "m5" : 0,
    }
}


function toggleStartStopClasses(){
    let temp = start_stop_classes.active
    let text_tmp = start_stop_classes.active_text;
    start_stop_classes.active = start_stop_classes.inactive
    start_stop_classes.inactive = temp;
    start_stop_classes.active_text = start_stop_classes.inactive_text;
    start_stop_classes.inactive_text = text_tmp;
}

function switchStartStop(id){
    console.log(start_stop_classes.active);
    console.log(start_stop_classes.inactive);
    let element = document.getElementById(id);
    element.classList.remove(start_stop_classes.active);
    element.classList.add(start_stop_classes.inactive);
    element.innerHTML = start_stop_classes.inactive_text;
    toggleStartStopClasses();
}

function toggleProgressBarItem(id){
    let element = document.getElementById(id);
    let index = progressbar_classes.materials[id];
    element.classList.remove(progressbar_classes.states[index]);
    element.classList.add(progressbar_classes.states[index+1]);
    progressbar_classes.materials[id]++;
}

const progressbar_toggles = {value: 0};

function linearToggleProgressbar(){
    if (progressbar_toggles.value === 0){
        progressbar_toggles.value++;
        toggleProgressBarItem("m1");
    }
    else if (progressbar_toggles.value === 1){
        progressbar_toggles.value++;
        toggleProgressBarItem("m1");
        toggleProgressBarItem("m2");
    }
    else if (progressbar_toggles.value === 2){
        progressbar_toggles.value++;
        toggleProgressBarItem("m2");
        toggleProgressBarItem("m3");
    }
    else if (progressbar_toggles.value === 3){
        progressbar_toggles.value++;
        toggleProgressBarItem("m3");
        toggleProgressBarItem("m4");
    }
    else if (progressbar_toggles.value === 4){
        progressbar_toggles.value++;
        toggleProgressBarItem("m4");
        toggleProgressBarItem("m5");
    }
}

const d_zone = {
    state : [ 'hidden_element', 'visible_element'],
    current : 0
}