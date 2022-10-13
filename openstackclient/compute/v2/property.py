from osc_lib.command import command
from openstackclient.i18n import _
import json


class CreatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(CreatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            '--name',
            metavar='<NAME>',
            help=_('NAME'),
        )
        parser.add_argument(
            '--title',
            metavar='<TITLE>',
            help=_('TITLE'),
        )
        parser.add_argument(
            '--schema',
            metavar='<SCHEMA>',
            help=_('SCHEMA'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image

        try:
            schema = json.loads(parsed_args.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': parsed_args.name, 'title': parsed_args.title}
            fields.update(schema)
            kwargs = {"name": parsed_args.name, "title": parsed_args.title, "type": fields["type"], "enum": fields["enum"], "description": fields["description"]}

            metadata_object = image_client.create_metadef_property(parsed_args.namespace, **kwargs)

            # 출력
            column_headers = (
                'Property',
                'Value',
            )

            columns = (
                ("description", metadata_object.description),
                ("enum", metadata_object.enum),
                ("name", metadata_object.name),
                ("title", metadata_object.title),
                ("type", metadata_object.type),
            )

            table = (
                column_headers,
                (
                    columns
                ),
            )
            return table


class DeletePropertyMd(command.Lister):
    _description = _("md-property-delete")

    def get_parser(self, prog_name):
        parser = super(DeletePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        image_client.delete_metadef_property(parsed_args.property_name, parsed_args.namespace)
        raise SystemExit


class ShowPropertyMd(command.Lister):
    _description = _("md-property-show")

    def get_parser(self, prog_name):
        parser = super(ShowPropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        metadata_object = image_client.get_metadef_property(parsed_args.property_name, parsed_args.namespace)

        # 출력

        column_headers = (
            'Property',
            'Value',
        )

        columns = (
            ("description", metadata_object.description),
            ("enum", metadata_object.enum),
            ("name", metadata_object.name),
            ("title", metadata_object.title),
            ("type", metadata_object.type),
        )

        table = (
            column_headers,
            (
                columns
            ),
        )
        return table


class UpdatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(UpdatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        parser.add_argument(
            '--name',
            metavar='<NAME>',
            help=_('NAME'),
        )
        parser.add_argument(
            '--title',
            metavar='<TITLE>',
            help=_('TITLE'),
        )
        parser.add_argument(
            '--schema',
            metavar='<SCHEMA>',
            help=_('SCHEMA'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image

        try:
            schema = json.loads(parsed_args.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': parsed_args.name, 'title': parsed_args.title}
            fields.update(schema)

            kwargs = {"name": parsed_args.name, "title": parsed_args.title, "type": fields["type"], "enum": fields["enum"], "description": fields["description"]}
            metadata_object = image_client.update_metadef_property(parsed_args.property_name, parsed_args.namespace, **kwargs)

            # 출력
            column_headers = (
                'Property',
                'Value',
            )

            columns = (
                ("description", metadata_object.description),
                ("enum", metadata_object.enum),
                ("name", metadata_object.name),
                ("title", metadata_object.title),
                ("type", metadata_object.type),
            )

            table = (
                column_headers,
                (
                    columns
                ),
            )
            return table


class ListPropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(ListPropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        metadata_object = image_client.metadef_properties(parsed_args.namespace)

        column_headers = (
            'name',
            'title',
            'type',
        )

        columns = (

        )

        for metadef in metadata_object.properties:
            column = (
                (
                    metadata_object.properties[metadef]["name"],
                    metadata_object.properties[metadef]["title"],
                    metadata_object.properties[metadef]["type"],
                ),
            )
            columns += column


        table = (
            column_headers,
            (
                columns
            ),
        )

        return table