// uses cotton/ui/toast.html

const TIME_VISIBLE = 5000;
const ANIMATION_IN = "appears-500"
const ANIMATION_OUT = "disappears-500"

const statusStyles = {
    error: {
        "css_class":"toast-error",
        "css_icon_selector":"#error-icon"
    },
    success: {
        "css_class":"toast-success",
        "css_icon_selector":"#success-icon"
    }
}

export default function CustomToast({template_id, data}) {
    // extract the fragment wich has the toast and svg icon elemnts
    const template = document.getElementById(template_id);
    const fragment =  document.importNode(template.content, true);
    const toast = fragment.querySelector('#toast'); 
    
    // chose styles to be used based in the status response 
    const statusObjStyles = data.status === 200 ? statusStyles.success : statusStyles.error;

    // fill toast with message and styles
    toast.classList.add(statusObjStyles.css_class)
    toast.querySelector('#svg-placeholder').innerHTML = fragment.querySelector(statusObjStyles.css_icon_selector).outerHTML;
    toast.querySelector('#message-placeholder').innerHTML = data.message;
   
    // displaying toast message
    document.body.appendChild(toast);
    
    // reset animation
    void toast.offsetWidth;

    // removing toast when animation ends
    setTimeout(() => {
    toast.classList.remove(ANIMATION_IN);
    void toast.offsetWidth;
    toast.classList.add(ANIMATION_OUT);
    toast.onanimationend = () => toast.remove();

    },TIME_VISIBLE);
}