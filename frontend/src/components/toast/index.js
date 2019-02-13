import vue from 'vue'
import toastComponent from './toast.vue'


const ToastContructor = vue.extend(toastComponent);


function showToast(text, duration = 2000){
    const toastDom = new ToastContructor({
        el: document.createElement('div'),
        data(){
            return {
                text:text,
                showWrap:true,
                showContent:true
            }
        }

    })


    document.body.appendChild(toastDom.$el)
    setTimeout(() => {toastDom.showWrap = false}, duration)
}

function registryToast(){
    vue.prototype.$toast = showToast
}

export default registryToast


