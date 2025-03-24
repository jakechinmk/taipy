import taipy as tp
from taipy.gui import Gui, Markdown, State
from taipy.gui import notify, navigate

login_status = False
username = ""
password = ""

login_md = Markdown('login.md')
parameters_md = Markdown('parameters.md')


def on_login(state:State):
    if state.username == 'admin' and state.password == 'password':
        state.login_status = True
        notify(state, 'success', 'Logged in!')
        navigate(state, to='parameters')
    else:
        notify(state, 'error', "Wrong username or password")

def on_logout(state:State):
    state.username = ""
    state.password = ""
    state.login_status = False
    notify(state, 'success', 'Logged out!')

pages_dict = {
    '/':login_md,
    'parameters': parameters_md
}

gui = Gui(pages=pages_dict)

if __name__ == '__main__':
    tp.Orchestrator().run()
    gui.run()
