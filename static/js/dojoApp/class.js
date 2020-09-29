define([
    "dojo/_base/declare",
    "dojo/request",
    "dijit/_WidgetBase",
    "dijit/_OnDijitClickMixin",
    "dijit/_TemplatedMixin",
    "dijit/layout/ContentPane",
    '_class_create',
    '_class_list',
    "dojo/domReady!"
], function (declare, request, _WidgetBase, _OnClickDijitMixin, _TemplatedMixin, ContentPane, ClassCreate, ClassList) {

    let classCreate = new ClassCreate()
    let classList = new ClassList()

    let contentPage = new ContentPane({title: "Class"})
    contentPage.addChild(classCreate)
    contentPage.addChild(classList)
    return contentPage
});
