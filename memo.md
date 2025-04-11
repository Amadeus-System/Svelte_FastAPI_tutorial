

## How to setup conda environment for FastAPI and svelte

``` Shell
conda create --name <env_name> python==3.10.4 --yes
conda activate <env_name>

python --version     # 3.10.4 (by "1-02 파이썬 설치하기")
pip install fastapi  # (by "1-03 FastAPI 개발 환경 준비하기")

# (Optional: when pip is not latest) python -m pip install --upgrade pip

# (env_name) c:/projects/<myapi> 도달하기 (by "1-04 FastAPI 프로젝트 생성하기")

# fastapi 구동할 서버 필요하므로 설치 (by "1-07 안녕하세요 파이보")
pip install "uvicorn[standard]"

```


``` Shell
# Frontend: Node.js 설치하기 (npm도 함께 설치됨)
# Node.js 설치: https://nodejs.org/ko

# Svelte 개발 환경 준비하기
(myapi) c:/projects/myapi> npm create vite@latest frontend -- --template svelte
Scaffolding project in ... 
Done. Now run:

  cd frontend
  npm install
  npm run dev
```

그리고 다음과 같이 frontend 디렉터리로 이동한 후에 Svelte 애플리케이션을 설치하자.

``` Bash
(myapi) c:/projects/myapi> cd frontend
(myapi) c:/projects/myapi> npm install # node_modules 폴더 생성됨
added 27 packages, and audited 28 packages in 3s

5 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

* Svelte for VSCode extension (in vscode) 설치하기
* 타입스크립트 사용하지 않으므로, 자바스크립트 타입 체크 설정 풀기
  ``` Shell
  # projects/myapi/frontend/jsconfig.json
  "checkJS": false
  ```

* frontend 서버 실행
  ``` Shell
  frontend & npm run dev
  ```

* alembic.ini에서 URL 설정할 때 뒤에 주석이 붙으면 에러 발생 ㅡㅡ;
  # driver://user:pass@localhost/dbname
  sqlalchemy.url = sqlite:///./myapi_2.db