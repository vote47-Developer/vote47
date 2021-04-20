const startPage = new StartPage();
const quizPage = new QuizPage();
const resultPage = new ResultPage();

function Router() {
  this.route = async path => {
    if (!history.state || path !== history.state.path) history.pushState({ path }, '', path);
    if (path === '') {
      startPage.init();
      app.innerHTML = '';
      app.appendChild(startPage.target);
    } else if (path === 'quiz') {
      await quizPage.init();
      app.innerHTML = '';
      app.appendChild(quizPage.target);
    } else if (path === 'result') {
      window.location = 'http://127.0.0.1:8000/candidate';
    }
  };
}

const router = new Router();
const app = document.querySelector('#app');

router.route(location.pathname.replace('/', ''));
window.addEventListener('popstate', () => {
  router.route(location.pathname.replace('/', ''));
});
