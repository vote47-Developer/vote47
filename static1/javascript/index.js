const startPage = new StartPage()
const quizPage = new QuizPage()
const resultPage = new ResultPage()

function Router() {
	this.route = async (path) => {
		// history.state 가 false 이거나 
		if (!history.state || path !== history.state.path)
			history.pushState({ path }, '', path)
 
		if (path === '') {
			startPage.init()
			app.innerHTML = ''
			app.appendChild(startPage.target)
		} else if (path === 'quiz') {
			await quizPage.init()
			app.innerHTML = ''
			app.appendChild(quizPage.target)
		} else if (path === 'result') {
			// const resultList = quizPage.getResultList()
			// // 퀴즈의 개수가 0개라면 quiz 로 다시 route tlzl
			// if (resultList.length === 0) {
			// 	this.route('quiz')
			// 	return
			// }
			// resultPage.init(resultList)
			// app.innerHTML = ''
			// app.appendChild(resultPage.target)
			window.location = "http://127.0.0.1:8000/candidate"
		}
	}
}

// router 생성
// 생성자 함수에 의한 객체 생성
const router = new Router()
const app = document.querySelector('#app')

router.route(location.pathname.replace('/', ''))
// history.pushState 를 통하여 새 데이터 전달을 위한 상태, 제목, url 지정
// ? window 의 객체의 popstate 이벤트를 이용
// window 객체의 location 프로퍼티는 현재 창에 표시된 문서의 URL 을 나타내는 Location 객체와 연결
// 이 객체에는 해당 창에 새 문서를 불러들이는 메서드도 존재한다.
// replace(url) : 새로운 주소 이동(세션 히스토리가 남지 않기 때문에 back버튼으로 이동 불가) 

window.addEventListener('popstate', () => {
	router.route(location.pathname.replace('/', ''))
})
