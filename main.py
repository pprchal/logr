import project.sinks.PAT
import project.gui.Application

if __name__ == '__main__':
    app = project.gui.Application.createGUI()
    project.sinks.PAT.PAT.start(app)
    app.mainloop()
