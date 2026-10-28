// ============================================================
//  Scratch 3.0 Custom Extension — List Range with Custom Join
//  Block: "list items [FROM] to [TO] of [LIST] joined by [SEP]"
// ============================================================

(function () {
  'use strict';

  class ListRangeExtension {
    getInfo() {
      return {
        id: 'listrange',
        name: 'List Range',
        color1: '#5C6BC0',
        color2: '#3949AB',
        color3: '#283593',
        blocks: [
          {
            opcode: 'getRange',
            blockType: Scratch.BlockType.REPORTER,
            text: 'list items [FROM] to [TO] of [LIST] joined by [SEP]',
            arguments: {
              FROM: {
                type: Scratch.ArgumentType.NUMBER,
                defaultValue: 1,
              },
              TO: {
                type: Scratch.ArgumentType.NUMBER,
                defaultValue: 5,
              },
              LIST: {
                type: Scratch.ArgumentType.STRING,
                menu: 'lists',
              },
              SEP: {
                type: Scratch.ArgumentType.STRING,
                defaultValue: ', ',
              },
            },
          },
        ],
        menus: {
          lists: {
            acceptReporters: true,
            items: '_getListNames',
          },
        },
      };
    }

    _getListNames() {
      const lists = this.runtime.getTargetForStage().getLists();
      return Object.keys(lists).map(name => ({
        text: name,
        value: name,
      }));
    }

    getRange(args, util) {
      const listName = args.LIST;
      const from = Math.max(1, Math.floor(Number(args.FROM) || 1));
      const to = Math.floor(Number(args.TO) || from);
      const sep = args.SEP === undefined ? ', ' : String(args.SEP);

      const target = util.target;
      const list = target.lookupOrCreateList(listName);
      if (!list || !list.value) return '';

      const items = list.value.slice(from - 1, to);
      return items.join(sep);
    }
  }

  Scratch.extensions.register(new ListRangeExtension());
})();
