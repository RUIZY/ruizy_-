import wx
import wx.xrc

# Tree 아이템 항목 작성 #
class MyTree(wx.TreeCtrl):
     def __init__(self, parent, id, position, size, style):
           wx.TreeCtrl.__init__(self, parent, id, position, size, style)
           root = self.AddRoot('HANBADA')
           blr = self.AppendItem(root, 'AUX.BOILER')
           icn = self.AppendItem(root, 'INCINERATOR')
           blr_burner = self.AppendItem(blr, 'BURNER')
           icn_burner = self.AppendItem(icn, 'BURNER')
           self.AppendItem(blr_burner, 'IGNITOR')
           self.AppendItem(blr_burner, 'FLAME EYE')
           self.AppendItem(icn_burner, 'IGNITOR')

# 메인 화면 (Frame) 작성 #      
class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1268,769 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.searchwindow = wx.SearchCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.searchwindow.ShowSearchButton( True )
		self.searchwindow.ShowCancelButton( False )
		bSizer1.Add( self.searchwindow, 0, wx.ALL, 5 )
		
		self.tree = MyTree( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,650 ), wx.TR_DEFAULT_STYLE )
		bSizer1.Add( self.tree, 0, wx.ALL, 5 )
		
		self.panel1.SetSizer( bSizer1 )
		self.panel1.Layout()
		bSizer1.Fit( self.panel1 )
		gbSizer1.Add( self.panel1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
  
		self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.textbox = wx.StaticText( self.panel2, wx.ID_ANY, u"MACHINERY", wx.DefaultPosition, wx.Size( 1000,690 ), 0 )
		self.textbox.Wrap( -1 )
		self.textbox.SetFont( wx.Font( 12, 75, 90, 92, False, "굴림" ) )
		self.textbox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2.Add( self.textbox, 0, wx.ALL, 5 )
		
		
		self.panel2.SetSizer( bSizer2 )
		self.panel2.Layout()
		bSizer2.Fit( self.panel2 )
		gbSizer1.Add( self.panel2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		self.menubar1 = wx.MenuBar( 0 )
		self.menu2 = wx.Menu()
		self.menuItem1 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Export to Excel", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu2.AppendItem( self.menuItem1 )
		
		self.menubar1.Append( self.menu2, u"Export" ) 
		
		self.menu3 = wx.Menu()
		self.menuItem2 = wx.MenuItem( self.menu3, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu3.AppendItem( self.menuItem2 )
		
		self.menubar1.Append( self.menu3, u"Help" ) 
		
		self.SetMenuBar( self.menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

app = wx.App(False) 
frame = MyFrame1(None) 
frame.Show(True) 

#start the applications 
app.MainLoop() 	