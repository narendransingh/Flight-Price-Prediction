function preventDupes( select, index ) {
    var options = select.options,
        len = options.length;
    while( len-- ) {
        options[ len ].disabled = false;
    }
    select.options[ index ].disabled = true;
    if( index === select.selectedIndex ) {
        alert('You\'ve already selected the item "' + select.options[index].text + '".\n\nPlease choose another.');
        this.selectedIndex = 0;
    }
}

var select1 = select = document.getElementById( 'Source' );
var select2 = select = document.getElementById( 'Destination' );

select1.onchange = function() {
    preventDupes.call(this, select2, this.selectedIndex );
};

select2.onchange = function() {
    preventDupes.call(this, select1, this.selectedIndex );
};
