define([
    "dijit/layout/TabContainer",
    'class',
    "dojo/_base/window",
    "dojo/dom-construct"], function (TabContainer,
                                     classContainer,
                                     win,
                                     domConstruct) {

    let tabContainer = new TabContainer({
        style: "margin-left: 10px; margin-right: 10px"
    });

    domConstruct.place(tabContainer.domNode, win.body());

    tabContainer.addChild(classContainer);

    tabContainer.startup();
})