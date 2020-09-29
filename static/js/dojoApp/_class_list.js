define([
    "dojox/grid/DataGrid",
    "dojo/store/Memory",
    "dojo/data/ObjectStore",
    "dojo/dom",
    "dijit/registry",
    "dojo/_base/declare",
    "dojo/request",
    "dijit/_WidgetBase",
    "dijit/_OnDijitClickMixin",
    "dijit/_TemplatedMixin",
    "dijit/layout/ContentPane",
    "dojo/domReady!"
], function (DataGrid, Memory, ObjectStore, dom, registry, declare, request, _WidgetBase, _OnClickDijitMixin, _TemplatedMixin, ContentPane) {

    return declare('ClassList', [_WidgetBase, _OnClickDijitMixin, _TemplatedMixin], {
        data: [],
        // language=HTML
        templateString: `
            <div>
                <h4>List class</h4>
                <div id="grid"></div>
            </div>
        `,
        id: "showClassContainer",
        title: "Class",
        postCreate: function () {
            request.get("/api/class/", {
                handleAs: 'json'
            }).then((res) => {
                let dataStore = new ObjectStore({objectStore: new Memory({data: res})});

                let grid = new DataGrid({
                    store: dataStore,
                    query: {},
                    queryOptions: {},
                    structure: [
                        {name: "ID", field: "id", width: "40%"},
                        {name: "Name", field: "name", width: "50%"},
                        {name: "Student", field: "number_of_student", width: "10%"},
                    ]
                }, "grid");
                grid.startup();
            })
        }
    });
});