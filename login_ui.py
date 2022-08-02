import kivy
from kivy.app import App
from kivymd.app import MDApp
#from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
#from kivy.uix.scatter import Scatter
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


KV='''
MDTextField:
   hint_text: "ENTER YOUR PHONE NUMBER"
   helper_text: "ENTER 10 DIGIT MOBILE NUMBER WITH COUNTRY CODE"
   helper_text_mode: "on_focus"
   icon_right: 'cellphone'
   icon_right_color:app.theme_cls.primary_color
   pos_hint: {"center_x":0.5,'center_y':0.6}
   size_hint_x:None
   width:300
'''

passwd='''
MDTextField:
   hint_text: "ENTER YOUR PASSWORD"
   helper_text: "MINIMUM 7 CHARECTERS"
   helper_text_mode: "on_focus"
   icon_right: 'key'
   icon_right_color:app.theme_cls.primary_color
   pos_hint: {"center_x":0.5,'center_y':0.4}
   size_hint_x:None
   width:300




'''
image = '''
Image:
    source: "LOGO.png"
    pos_hint: {"center_x":0.5,"center_y":0.8}
    size_hint_x: None
    width: 300
    size_hint: .1, .5
'''



class Login(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= 'Blue'
        self.theme_cls.theme_style="Light"
        self.username= Builder.load_string(KV)
        #username = MDTextField(text="ENTER MOBILE NUMBER",
                               #pos_hint={'center_x':0.5 ,'center_y':0.6},
                               #size_hint_x=None,width=300
                               
                               #

        self.password = Builder.load_string(passwd)
        #password = MDTextField(text="ENTER PASSWORD",
                               #pos_hint={'center_x':0.5 ,'center_y':0.4},
                               #size_hint_x=None,width=300
                               #)
                               
                               
        images = Builder.load_string(image)
                               
        button = MDRectangleFlatButton(text = 'LOGIN',pos_hint={'center_x':0.5,'center_y':0.10},on_release=self.login)
        #button1 = MDRectangleFlatButton(text = 'LOGIN',pos_hint={'center_x':0.5,'center_y':0.10},on_release=self.pass_check)
       
      
        screen.add_widget(self.username)
        screen.add_widget(images)
        screen.add_widget(self.password)
        screen.add_widget(button)
        #screen.add_widget(button1)
       
        
        return screen

    def login(self, obj):
        if self.username.text is "":
            check_string ='PLEASE ENTER MOBILE NUMBER'
        else:
            check_string = self.username.text + ' PHONE NUMBER DOES NOT EXIST'
        close_button = MDFlatButton(text = 'RETRY',on_release=self.close_dialog)
        self.dialog = MDDialog(title='ACCOUNT CHECK',text = check_string,
                               size_hint=(0.7,1),
                               buttons=[close_button]
                               )
        
    
        self.dialog.open()
        
        
    #def pass_check(self, obj):
        #if self.password.text is "":
            #check_string ='PLEASE ENTER PASSWORD'
       # else:
       #     check_string = self.password.text + ' WRONG PASSWORD'
        #close_button = MDFlatButton(text = 'RETRY',on_release=self.close_dialog)
        #self.dialog = MDDialog(title='ACCOUNT CHECK',text = check_string,
         #                      size_hint=(0.7,1),
          #                     buttons=[close_button]
           #                    )
        
    
      #  self.dialog.open()    
        
    def close_dialog(self, obj):
        self.dialog.dismiss()
        
        
        
                
if __name__ == "__main__":
    Login().run()
