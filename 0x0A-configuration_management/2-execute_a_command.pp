# Create a manifest that kills a process named killmenow
exec { 'Run a pkill command to kill a killmenow process	':
  command => '/usr/bin/pkill -9 killmenow',
}