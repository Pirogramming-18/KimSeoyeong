let timer;
let timer_status=false;

let second=0;
let milliSecond=0;

const checkAllBtn=document.querySelectorAll('.check-all');

const startBtn=document.querySelector('#startBtn');
const stopBtn=document.querySelector('#stopBtn');
const resetBtn=document.querySelector('#resetBtn');

const deleteBtn=document.querySelector('#deleteBtn');

const displaySecond=document.querySelector('#second');
const displayMilliSecond=document.querySelector('#milliSecond');

const recordField=document.querySelector('#recordField');

//timer-control 버튼 관리 (start, stop,)

//start 버튼 누르면 실행
function startTimer(){
    milliSecond++;
    if(milliSecond>=99){
        milliSecond=0;
        second++;
        displaySecond.textContent=second>10? second:'0'+second;
    }
    displayMilliSecond.textContent=milliSecond>10? milliSecond:'0'+milliSecond;
    
    if(timer_status) return;
    timer_status=true;
};

startBtn.onclick=()=>{
    clearInterval(timer);
    timer=setInterval(startTimer,10);
};

stopBtn.onclick=()=>{
    clearInterval(timer);
    addRecordField();
    selectOneBtn = document.querySelector('#recordField');
    selectOneBtn.removeEventListener('click', selectBtnClick);
    selectOneBtn.addEventListener('click', selectBtnClick);
    length++;
    checkFull();
}

resetBtn.onclick = () => {
    clearInterval(timer);
    second = 0;
    milliSecond= 0;
    displaySecond.textContent = "00";
    displayMilliSecond.textContent = "00";
};

//구간기록 추가
function addRecordField(){
    recordField.innerHTML+= `
    <li class="record">
        <input type="checkbox" class="check">
        <div>
            <span id="sec">${displaySecond.textContent}</span>
            <span>:</span>
            <span id="m-sec">${displayMilliSecond.textContent}</span>
        </div>
    </li>
    `
};
