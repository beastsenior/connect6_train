#from shower import Cshower
#app=Cshower()
#app.mainloop()

import trainer
print(trainer.matrix)
#print(trainer.savemove)
#trainer.move_human()
#print(trainer.matrix)
#print(trainer.savemove)
#print('ok')
trainer.move_random(-1)
print(trainer.position)
#print(trainer.moveposition)
#print(trainer.nextposition)
print(trainer.savemove[trainer.savecount - 1])
print(trainer.matrix)




##########################
#m=[[0,0,1,1],[1,0,0,1],[0,0,0,0],[-1,-1,-1,-1]]
#app.redraw(m)
#app.canvas.itemconfig(app.oval, state='hidden')
#app.canvas.move(app.oval, 10, 10)