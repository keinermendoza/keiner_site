// there are many assumptions here 
// toast element has the class toast
// SUCCESS_CLASS is present in the toast element

export default function CustomToast({template_id, data}) {
    const SUCCESS_CLASS = "bg-cyan-400";
    const ERROR_CLASS = "bg-yellow-300";
    const TIME_VISIBLE = 5000;
    const ANIMATION_IN = "appears-500"
    const ANIMATION_OUT = "disappears-500"

    const template = document.getElementById(template_id);
    const fragment = template.content.cloneNode(true);
    const toast = fragment.querySelector(".toast");

    // changing icon and color when not sucessful status
    if (data.status !== 200) {
    toast.querySelector("#toast-svg-icon").src = toast.querySelector("#toast-svg-icon").src.replace('check-badge.svg', 'danger.svg');
    toast.classList.remove(SUCCESS_CLASS);
    toast.classList.add(ERROR_CLASS);
    }
    // displaying toast message
    toast.querySelector("#toast-text-message").innerHTML = data.message;
    document.body.appendChild(toast);
    void toast.offsetWidth;

    // removing toast
    setTimeout(() => {
    toast.classList.remove(ANIMATION_IN);
    void toast.offsetWidth;
    toast.classList.add(ANIMATION_OUT);
    toast.onanimationend = () => toast.remove();

    },TIME_VISIBLE);
}