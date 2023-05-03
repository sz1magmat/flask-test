const { app, BrowserWindow, screen } = require('electron');
const windowStateKeeper = require('electron-window-state');

function createWindow()
{
    const { width, height } = screen.getPrimaryDisplay().workAreaSize;

    let mainWindowState = windowStateKeeper(
    {
        defaultWidth: width,
        defaultHeight: height,
    });

    const win = new BrowserWindow(
    {
        show: false,
        x: mainWindowState.x,
        y: mainWindowState.y,
        icon: 'assets/icon.ico',
        width: mainWindowState.width,
        height: mainWindowState.height,

        webPreferences:
        {
            nodeIntegration: false,
            contextIsolation: true,
        },
    });

    mainWindowState.manage(win);

    win.setMenuBarVisibility(false);
    win.loadURL('https://proj-aums.hu/');

    win.once('ready-to-show', () =>
    { win.show(); });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () =>
{ if (process.platform !== 'darwin') app.quit(); });

app.on('activate', () =>
{ if (BrowserWindow.getAllWindows().length === 0) createWindow(); });