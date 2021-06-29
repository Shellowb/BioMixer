Dropzone.autoDiscover = false

const myDropzone = new Dropzone("#my-dropzone", {
    maxFilesize: 2,
    acceptedFiles: '.csv',
    autoProcessQueue: false,
    addRemoveLinks: true,
    display: true
})

function process() {
    myDropzone.processQueue()
    //myDropzone.visible = false
}

// function closeDropZone() {
//     document.location.href = '/dzone_success'
// }