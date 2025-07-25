import os
import json
import secrets
import string
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
# Note: kivy.clipboard not available on Android

ROOMS_DIR = "rooms"
os.makedirs(ROOMS_DIR, exist_ok=True)

class ConnectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_app = None
        
        # Create scrollable main layout for mobile
        scroll = ScrollView()
        
        # Main layout with proper mobile spacing
        layout = BoxLayout(
            orientation='vertical', 
            spacing=20,  # Increased from 15
            padding=[25, 50, 25, 25],  # More padding
            size_hint_y=None
        )
        layout.bind(minimum_height=layout.setter('height'))

        # App title with more space
        title = Label(
            text='MQTT Chat App', 
            font_size='28sp',  # Larger font
            size_hint_y=None, 
            height='80dp',  # Taller
            color=[1, 1, 1, 1]
        )
        layout.add_widget(title)

        # Username section with better spacing
        username_label = Label(
            text='Your Username:', 
            size_hint_y=None, 
            height='45dp',  # Taller labels
            font_size='18sp'  # Larger font
        )
        layout.add_widget(username_label)
        
        self.username_input = TextInput(
            text='User',
            size_hint_y=None, 
            height='55dp',  # Much taller inputs
            font_size='18sp',  # Larger font
            multiline=False,
            padding=[10, 15]  # Internal padding
        )
        layout.add_widget(self.username_input)

        # Spacer
        layout.add_widget(Label(size_hint_y=None, height='10dp'))

        # Server address section
        server_label = Label(
            text='Server Address:', 
            size_hint_y=None, 
            height='45dp',
            font_size='18sp'
        )
        layout.add_widget(server_label)
        
        self.server_input = TextInput(
            text='localhost',
            size_hint_y=None, 
            height='55dp',
            font_size='18sp',
            multiline=False,
            padding=[10, 15]
        )
        layout.add_widget(self.server_input)

        # Port section
        port_label = Label(
            text='Port:', 
            size_hint_y=None, 
            height='45dp',
            font_size='18sp'
        )
        layout.add_widget(port_label)
        
        self.port_input = TextInput(
            text='1883',
            size_hint_y=None, 
            height='55dp',
            font_size='18sp',
            multiline=False,
            input_filter='int',
            padding=[10, 15]
        )
        layout.add_widget(self.port_input)

        # Room name section
        room_label = Label(
            text='Chat Room Name:', 
            size_hint_y=None, 
            height='45dp',
            font_size='18sp'
        )
        layout.add_widget(room_label)
        
        self.room_input = TextInput(
            text='general',
            size_hint_y=None, 
            height='55dp',
            font_size='18sp',
            multiline=False,
            padding=[10, 15]
        )
        layout.add_widget(self.room_input)

        # Big spacer before MQTT auth
        layout.add_widget(Label(size_hint_y=None, height='25dp'))

        # MQTT Authentication section header
        mqtt_auth_header = Label(
            text='MQTT Authentication (Optional)',
            size_hint_y=None,
            height='40dp',
            font_size='16sp',
            italic=True,
            color=[0.8, 0.8, 0.8, 1]
        )
        layout.add_widget(mqtt_auth_header)

        # MQTT Username
        mqtt_user_label = Label(
            text='MQTT Username:', 
            size_hint_y=None, 
            height='40dp',
            font_size='16sp'
        )
        layout.add_widget(mqtt_user_label)
        
        self.mqtt_username_input = TextInput(
            size_hint_y=None, 
            height='50dp',
            font_size='16sp',
            multiline=False,
            padding=[10, 12]
        )
        layout.add_widget(self.mqtt_username_input)
        
        # MQTT Password
        mqtt_pass_label = Label(
            text='MQTT Password:', 
            size_hint_y=None, 
            height='40dp',
            font_size='16sp'
        )
        layout.add_widget(mqtt_pass_label)
        
        self.mqtt_password_input = TextInput(
            password=True,
            size_hint_y=None, 
            height='50dp',
            font_size='16sp',
            multiline=False,
            padding=[10, 12]
        )
        layout.add_widget(self.mqtt_password_input)
        
        # Show MQTT password toggle
        mqtt_toggle_layout = BoxLayout(
            orientation='horizontal', 
            size_hint_y=None, 
            height='50dp',
            spacing=15
        )
        mqtt_toggle_label = Label(
            text='Show MQTT Password:', 
            size_hint_x=0.7,
            font_size='16sp'
        )
        self.show_mqtt_password = CheckBox(size_hint_x=0.3, size_hint_y=None, height='40dp')
        self.show_mqtt_password.bind(active=self.toggle_mqtt_password_visibility)
        mqtt_toggle_layout.add_widget(mqtt_toggle_label)
        mqtt_toggle_layout.add_widget(self.show_mqtt_password)
        layout.add_widget(mqtt_toggle_layout)
        
        # Help text
        help_label = Label(
            text='Leave blank for anonymous connection',
            size_hint_y=None,
            height='35dp',
            font_size='14sp',
            color=[0.6, 0.6, 0.6, 1]
        )
        layout.add_widget(help_label)

        # Big spacer before encryption
        layout.add_widget(Label(size_hint_y=None, height='25dp'))

        # Encryption key section with generate button
        key_label = Label(
            text='Encryption Key:', 
            size_hint_y=None, 
            height='45dp',
            font_size='18sp'
        )
        layout.add_widget(key_label)
        
        # Key input and generate button in horizontal layout
        key_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height='55dp',
            spacing=15
        )
        
        self.key_input = TextInput(
            password=True,
            size_hint_x=0.7,
            font_size='16sp',
            multiline=False,
            padding=[10, 15]
        )
        
        self.generate_key_button = Button(
            text='Generate',
            size_hint_x=0.3,
            font_size='16sp',
            size_hint_y=None,
            height='55dp'
        )
        self.generate_key_button.bind(on_release=self.generate_key)
        
        key_layout.add_widget(self.key_input)
        key_layout.add_widget(self.generate_key_button)
        layout.add_widget(key_layout)

        # Show key and copy buttons
        key_controls = BoxLayout(
            orientation='horizontal', 
            size_hint_y=None, 
            height='60dp',
            spacing=15
        )
        
        # Show key toggle
        show_layout = BoxLayout(
            orientation='horizontal',
            size_hint_x=0.6,
            spacing=10
        )
        show_label = Label(
            text='Show Key:', 
            size_hint_x=0.7,
            font_size='16sp'
        )
        self.show_key = CheckBox(size_hint_x=0.3, size_hint_y=None, height='40dp')
        self.show_key.bind(active=self.toggle_key_visibility)
        show_layout.add_widget(show_label)
        show_layout.add_widget(self.show_key)
        
        # Copy key button
        self.copy_key_button = Button(
            text='Copy Key',
            size_hint_x=0.4,
            font_size='16sp',
            size_hint_y=None,
            height='55dp'
        )
        self.copy_key_button.bind(on_release=self.copy_key)
        
        key_controls.add_widget(show_layout)
        key_controls.add_widget(self.copy_key_button)
        layout.add_widget(key_controls)

        # Big spacer before saved rooms
        layout.add_widget(Label(size_hint_y=None, height='30dp'))

        # Saved rooms section
        saved_label = Label(
            text='Saved Rooms:', 
            size_hint_y=None, 
            height='45dp',
            font_size='18sp'
        )
        layout.add_widget(saved_label)
        
        self.room_spinner = Spinner(
            text='Load Room',
            values=self.get_saved_rooms(),
            size_hint_y=None, 
            height='55dp',
            font_size='16sp'
        )
        self.room_spinner.bind(text=self.load_room)
        layout.add_widget(self.room_spinner)

        # Spacer
        layout.add_widget(Label(size_hint_y=None, height='20dp'))

        # Save and copy room buttons
        room_buttons = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height='70dp',
            spacing=15
        )
        
        self.save_button = Button(
            text='Save Room',
            size_hint_x=0.5,
            font_size='16sp',
            size_hint_y=None,
            height='65dp'
        )
        self.save_button.bind(on_release=self.save_room)
        
        self.copy_room_button = Button(
            text='Copy Config',
            size_hint_x=0.5,
            font_size='16sp',
            size_hint_y=None,
            height='65dp'
        )
        self.copy_room_button.bind(on_release=self.copy_room_config)
        
        room_buttons.add_widget(self.save_button)
        room_buttons.add_widget(self.copy_room_button)
        layout.add_widget(room_buttons)

        # Big spacer
        layout.add_widget(Label(size_hint_y=None, height='25dp'))

        # Connect button - make it prominent
        self.connect_button = Button(
            text='Connect to Chat Room',
            size_hint_y=None, 
            height='80dp',  # Extra tall for main action
            font_size='20sp'  # Larger font
        )
        self.connect_button.bind(on_release=self.connect)
        layout.add_widget(self.connect_button)

        # Bottom padding
        layout.add_widget(Label(size_hint_y=None, height='50dp'))

        scroll.add_widget(layout)
        self.add_widget(scroll)

    def set_main_app(self, app):
        """Set reference to main app"""
        self.main_app = app

    def toggle_mqtt_password_visibility(self, checkbox, value):
        """Toggle MQTT password visibility"""
        self.mqtt_password_input.password = not value

    def generate_key(self, instance):
        """Generate a new encryption key (like desktop version)"""
        try:
            from cryptography.fernet import Fernet
            key = Fernet.generate_key()
            self.key_input.text = key.decode()
            self.show_popup("New encryption key generated!")
        except ImportError:
            # Fallback to simple random key if cryptography not available
            key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
            self.key_input.text = key
            self.show_popup("New encryption key generated! (Install 'cryptography' package for stronger keys)")

    def copy_key(self, instance):
        """Copy the encryption key to clipboard (mobile-friendly)"""
        if self.key_input.text:
            # On mobile, just show the key in a popup for manual copying
            self.show_popup(f"Encryption Key:\n{self.key_input.text}\n\n(Long press to copy manually)")
        else:
            self.show_popup("No key to copy!")

    def copy_room_config(self, instance):
        """Copy room configuration as shareable text (mobile-friendly)"""
        config_text = f"""MQTT Chat Room Config:
Server: {self.server_input.text}
Port: {self.port_input.text}
Room: {self.room_input.text}
Key: {self.key_input.text if self.key_input.text else 'None'}"""
        
        # On mobile, show in popup for manual copying
        self.show_popup(f"Room Configuration:\n\n{config_text}\n\n(Long press to copy manually)")

    def toggle_key_visibility(self, checkbox, value):
        """Toggle password visibility for encryption key"""
        self.key_input.password = not value

    def get_saved_rooms(self):
        """Get list of saved room configurations"""
        try:
            return [f[:-5] for f in os.listdir(ROOMS_DIR) if f.endswith('.json')]
        except:
            return []

    def load_room(self, spinner, room_name):
        """Load a saved room configuration"""
        if room_name == 'Load Room':
            return
            
        file_path = os.path.join(ROOMS_DIR, f"{room_name}.json")
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                self.username_input.text = data.get("username", "User")
                self.server_input.text = data.get("server", "localhost")
                self.port_input.text = str(data.get("port", "1883"))
                self.room_input.text = data.get("room", "general")
                self.key_input.text = data.get("key", "")
                self.mqtt_username_input.text = data.get("mqtt_username", "")
                self.mqtt_password_input.text = data.get("mqtt_password", "")
        except Exception as e:
            self.show_popup(f"Error loading room: {e}")

    def save_room(self, instance):
        """Save current room configuration"""
        name = self.room_input.text.strip()
        if not name:
            self.show_popup("Room name is required!")
            return
            
        try:
            data = {
                "username": self.username_input.text.strip() or "User",
                "server": self.server_input.text.strip() or "localhost",
                "port": int(self.port_input.text.strip() or "1883"),
                "room": name,
                "key": self.key_input.text.strip(),
                "mqtt_username": self.mqtt_username_input.text.strip(),
                "mqtt_password": self.mqtt_password_input.text.strip()
            }
            
            file_path = os.path.join(ROOMS_DIR, f"{name}.json")
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
                
            # Update spinner values
            self.room_spinner.values = self.get_saved_rooms()
            self.show_popup("Room configuration saved!")
            
        except Exception as e:
            self.show_popup(f"Error saving room: {e}")

    def show_popup(self, message):
        """Show info popup with better mobile sizing"""
        popup_content = Label(
            text=message,
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='16sp'
        )
        
        popup = Popup(
            title='Information',
            content=popup_content,
            size_hint=(0.9, 0.6),  # Larger on mobile
            auto_dismiss=True
        )
        popup.open()

    def connect(self, instance):
        """Connect to MQTT broker"""
        # Validate inputs
        username = self.username_input.text.strip()
        server = self.server_input.text.strip()
        port = self.port_input.text.strip()
        room = self.room_input.text.strip()
        key = self.key_input.text.strip()
        
        if not username:
            self.show_popup("Username is required!")
            return
        
        if not server:
            self.show_popup("Server address is required!")
            return
            
        if not port:
            port = "1883"
            
        try:
            port_int = int(port)
            if port_int <= 0 or port_int > 65535:
                raise ValueError("Invalid port range")
        except ValueError:
            self.show_popup("Port must be a valid number (1-65535)!")
            return
            
        if not room:
            self.show_popup("Room name is required!")
            return
        
        # Connect via main app (now with MQTT auth)
        if self.main_app:
            # Pass username and MQTT auth to main app
            self.main_app.username = username
            mqtt_user = self.mqtt_username_input.text.strip()
            mqtt_pass = self.mqtt_password_input.text.strip()
            self.main_app.connect_to_mqtt(server, port_int, room, key, mqtt_user, mqtt_pass)
        else:
            self.show_popup("App not properly initialized!")

# For testing the connection screen standalone
if __name__ == '__main__':
    from kivy.app import App
    
    class TestApp(App):
        def build(self):
            return ConnectionScreen()
    
    TestApp().run()