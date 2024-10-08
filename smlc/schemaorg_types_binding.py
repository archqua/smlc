"""This file was automatically generated at 2024-09-24T08:59:10+00:00.

Documentation may not function properly.

Bindings for [schema.org types](
https://schema.org/docs/full.html).
"""

__docformat__ = "numpy"

import os
import pickle
from copy import deepcopy
from typing import Type, Union

import schemaorg.main

Schemaorg: Type = schemaorg.main.Schema


def _copyattrs(dst, src):
    for an, av in vars(src).items():
        setattr(dst, an, deepcopy(av))
    return dst


class Schema(Schemaorg):
    """Wrapper for `Schemaorg`.

    Prepends "sc:" to formatted type names.
    """

    def __init__(self, schema: Union[str, schemaorg.main.Schema], *args, **kwargs):
        if isinstance(schema, schemaorg.main.Schema):
            schelf = schema
        else:
            schelf = schemaorg.main.Schema(schema, *args, **kwargs)
        _copyattrs(self, schelf)

    def __str__(self):
        return "sc:" + super(Schema, self).__str__()

    def __repr__(self):
        return str(self)


with open(os.path.join("smlc", "schemaorg_types_storage.pkl"), "rb") as sf:
    schema_storage = pickle.load(sf)


class sc:
    """Convenient namespace. Usage: `sc.TypeName` instead of `Schema("TypeName")`.

    Special cases: `_True`, `_False` and `_3DModel` are prepended with `_` for pythonic reasons.
    """

    def parse(tn: str, sep=":", raise_not_sc: bool = True):
        """`'sc:TypeName'` to `sc.TypeName`"""
        tkns = tn.split(":")
        if raise_not_sc:
            assert tkns[0] == "sc", "Type annotation must start with 'sc:'"
        t = tkns[-1]
        if t in ["True", "False", "3DModel"]:
            t = "_" + t
        return getattr(sc, t)

    _3DModel = Schema(schema_storage["3DModel"])
    """@public A 3D model represents some kind of 3D content, which may have <a class="localLink" href="#sc.encoding">encoding</a>s in one or more <a class="localLink" href="#sc.MediaObject">MediaObject</a>s. Many 3D formats are available (e.g. see <a href="https://en.wikipedia.org/wiki/Category:3D_graphics_file_formats">Wikipedia</a>); specific encoding formats can be represented using the <a class="localLink" href="#sc.encodingFormat">encodingFormat</a> property applied to the relevant <a class="localLink" href="#sc.MediaObject">MediaObject</a>. For the
case of a single file published after Zip compression, the convention of appending '+zip' to the <a class="localLink" href="#sc.encodingFormat">encodingFormat</a> can be used. Geospatial, AR/VR, artistic/animation, gaming, engineering and scientific content can all be represented using <a class="localLink" href="#sc.3DModel">3DModel</a>."""
    AMRadioChannel = Schema(schema_storage["AMRadioChannel"])
    """A radio channel that uses AM."""
    APIReference = Schema(schema_storage["APIReference"])
    """Reference documentation for application programming interfaces (APIs)."""
    Abdomen = Schema(schema_storage["Abdomen"])
    """Abdomen clinical examination."""
    AboutPage = Schema(schema_storage["AboutPage"])
    """Web page type: About page."""
    AcceptAction = Schema(schema_storage["AcceptAction"])
    """The act of committing to/adopting an object.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.RejectAction">RejectAction</a>: The antonym
    of AcceptAction.</li> </ul>
    """
    Accommodation = Schema(schema_storage["Accommodation"])
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room,
    a camping pitch, or a meeting room.

    Many accommodations are for overnight stays, but this is not a mandatory
    requirement. For more specific types of accommodations not defined in schema.org,
    one can use additionalType with external vocabularies. <br /><br /> See also the <a
    href="/docs/hotels.html">dedicated document on the use of schema.org for marking up
    hotels and other forms of accommodations</a>.
    """
    AccountingService = Schema(schema_storage["AccountingService"])
    """Accountancy business.<br/><br/>

    As a <a class="localLink" href="#sc.LocalBusiness">LocalBusiness</a> it can be
    described as a <a class="localLink" href="#sc.provider">provider</a> of one or more
    <a class="localLink" href="#sc.Service">Service</a>(s).
    """
    AchieveAction = Schema(schema_storage["AchieveAction"])
    """The act of accomplishing something via previous efforts.

    It is an instantaneous action rather than an ongoing process.
    """
    Action = Schema(schema_storage["Action"])
    """An action performed by a direct agent and indirect participants upon a direct
    object. Optionally happens at a location with the help of an inanimate instrument.
    The execution of the action may produce a result. Specific action sub-type
    documentation specifies the exact expectation of each argument/role.<br/><br/>

    See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a> and <a href="https://schema.org/docs/actions.html">Actions overview document</a>.
    """
    ActionAccessSpecification = Schema(schema_storage["ActionAccessSpecification"])
    """A set of requirements that a must be fulfilled in order to perform an Action."""
    ActionStatusType = Schema(schema_storage["ActionStatusType"])
    """The status of an Action."""
    ActivateAction = Schema(schema_storage["ActivateAction"])
    """The act of starting or activating a device or application (e.g. starting a timer
    or turning on a flashlight)."""
    ActivationFee = Schema(schema_storage["ActivationFee"])
    """Represents the activation fee part of the total price for an offered product, for
    example a cellphone contract."""
    ActiveActionStatus = Schema(schema_storage["ActiveActionStatus"])
    """An in-progress action (e.g, while watching the movie, or driving to a
    location)."""
    ActiveNotRecruiting = Schema(schema_storage["ActiveNotRecruiting"])
    """Active, but not recruiting new participants."""
    AddAction = Schema(schema_storage["AddAction"])
    """The act of editing by adding an object to a collection."""
    AdministrativeArea = Schema(schema_storage["AdministrativeArea"])
    """A geographical region, typically under the jurisdiction of a particular
    government."""
    AdultEntertainment = Schema(schema_storage["AdultEntertainment"])
    """An adult entertainment establishment."""
    AdvertiserContentArticle = Schema(schema_storage["AdvertiserContentArticle"])
    """An <a class="localLink" href="#sc.Article">Article</a> that an external entity
    has paid to place or to produce to its specifications.

    Includes <a href="https://en.wikipedia.org/wiki/Advertorial">advertorials</a>, sponsored content, native advertising and other paid content.
    """
    AerobicActivity = Schema(schema_storage["AerobicActivity"])
    """Physical activity of relatively low intensity that depends primarily on the
    aerobic energy-generating process; during activity, the aerobic metabolism uses
    oxygen to adequately meet energy demands during exercise."""
    AggregateOffer = Schema(schema_storage["AggregateOffer"])
    """When a single product is associated with multiple offers (for example, the same
    pair of shoes is offered by different merchants), then AggregateOffer can be
    used.<br/><br/>

    Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined <a class="localLink" href="#sc.businessFunction">businessFunction</a> value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.
    """
    AggregateRating = Schema(schema_storage["AggregateRating"])
    """The average rating based on multiple ratings or reviews."""
    AgreeAction = Schema(schema_storage["AgreeAction"])
    """The act of expressing a consistency of opinion with the object.

    An agent agrees to/about an object (a proposition, topic or theme) with
    participants.
    """
    Airline = Schema(schema_storage["Airline"])
    """An organization that provides flights for passengers."""
    Airport = Schema(schema_storage["Airport"])
    """An airport."""
    AlbumRelease = Schema(schema_storage["AlbumRelease"])
    """AlbumRelease."""
    AlignmentObject = Schema(schema_storage["AlignmentObject"])
    """An intangible item that describes an alignment between a learning resource and a
    node in an educational framework.<br/><br/>

    Should not be used where the nature of the alignment can be described using a simple
    property, for example to express that a resource <a class="localLink"
    href="#sc.teaches">teaches</a> or <a class="localLink"
    href="#sc.assesses">assesses</a> a competency.
    """
    AllWheelDriveConfiguration = Schema(schema_storage["AllWheelDriveConfiguration"])
    """All-wheel Drive is a transmission layout where the engine drives all four
    wheels."""
    AllergiesHealthAspect = Schema(schema_storage["AllergiesHealthAspect"])
    """Content about the allergy-related aspects of a health topic."""
    AllocateAction = Schema(schema_storage["AllocateAction"])
    """The act of organizing tasks/objects/events by associating resources to it."""
    AmpStory = Schema(schema_storage["AmpStory"])
    """A creative work with a visual storytelling format intended to be viewed online,
    particularly on mobile devices."""
    AmusementPark = Schema(schema_storage["AmusementPark"])
    """An amusement park."""
    AnaerobicActivity = Schema(schema_storage["AnaerobicActivity"])
    """Physical activity that is of high-intensity which utilizes the anaerobic
    metabolism of the body."""
    AnalysisNewsArticle = Schema(schema_storage["AnalysisNewsArticle"])
    """An AnalysisNewsArticle is a <a class="localLink"
    href="#sc.NewsArticle">NewsArticle</a> that, while based on factual reporting,
    incorporates the expertise of the author/producer, offering interpretations and
    conclusions."""
    AnatomicalStructure = Schema(schema_storage["AnatomicalStructure"])
    """Any part of the human body, typically a component of an anatomical system.

    Organs, tissues, and cells are all anatomical structures.
    """
    AnatomicalSystem = Schema(schema_storage["AnatomicalSystem"])
    """An anatomical system is a group of anatomical structures that work together to
    perform a certain task.

    Anatomical systems, such as organ systems, are one organizing principle of anatomy,
    and can includes circulatory, digestive, endocrine, integumentary, immune,
    lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary,
    vestibular, and other systems.
    """
    Anesthesia = Schema(schema_storage["Anesthesia"])
    """A specific branch of medical science that pertains to study of anesthetics and
    their application."""
    AnimalShelter = Schema(schema_storage["AnimalShelter"])
    """Animal shelter."""
    Answer = Schema(schema_storage["Answer"])
    """An answer offered to a question; perhaps correct, perhaps opinionated or
    wrong."""
    Apartment = Schema(schema_storage["Apartment"])
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>)."""
    ApartmentComplex = Schema(schema_storage["ApartmentComplex"])
    """Residence type: Apartment complex."""
    Appearance = Schema(schema_storage["Appearance"])
    """Appearance assessment with clinical examination."""
    AppendAction = Schema(schema_storage["AppendAction"])
    """The act of inserting at the end if an ordered collection."""
    ApplyAction = Schema(schema_storage["ApplyAction"])
    """The act of registering to an organization/service without the guarantee to
    receive it.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.RegisterAction">RegisterAction</a>: Unlike
    RegisterAction, ApplyAction has no guarantees that the application will be
    accepted.</li> </ul>
    """
    ApprovedIndication = Schema(schema_storage["ApprovedIndication"])
    """An indication for a medical therapy that has been formally specified or approved
    by a regulatory body that regulates use of the therapy; for example, the US FDA
    approves indications for most drugs in the US."""
    Aquarium = Schema(schema_storage["Aquarium"])
    """Aquarium."""
    ArchiveComponent = Schema(schema_storage["ArchiveComponent"])
    """An intangible type to be applied to any archive content, carrying with it a set
    of properties required to describe archival items and collections."""
    ArchiveOrganization = Schema(schema_storage["ArchiveOrganization"])
    """An organization with archival holdings.

    An organization which keeps and preserves archival material and typically makes it
    accessible to the public.
    """
    ArriveAction = Schema(schema_storage["ArriveAction"])
    """The act of arriving at a place.

    An agent arrives at a destination from a fromLocation, optionally with participants.
    """
    ArtGallery = Schema(schema_storage["ArtGallery"])
    """An art gallery."""
    Artery = Schema(schema_storage["Artery"])
    """A type of blood vessel that specifically carries blood away from the heart."""
    Article = Schema(schema_storage["Article"])
    """An article, such as a news article or piece of investigative report. Newspapers
    and magazines have articles of many different types and this is intended to cover
    them all.<br/><br/>

    See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.
    """
    AskAction = Schema(schema_storage["AskAction"])
    """The act of posing a question / favor to someone.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ReplyAction">ReplyAction</a>: Appears
    generally as a response to AskAction.</li> </ul>
    """
    AskPublicNewsArticle = Schema(schema_storage["AskPublicNewsArticle"])
    """A <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> expressing an open
    call by a <a class="localLink"
    href="#sc.NewsMediaOrganization">NewsMediaOrganization</a> asking the public for
    input, insights, clarifications, anecdotes, documentation, etc., on an issue, for
    reporting purposes."""
    AssessAction = Schema(schema_storage["AssessAction"])
    """The act of forming one's opinion, reaction or sentiment."""
    AssignAction = Schema(schema_storage["AssignAction"])
    """The act of allocating an action/event/task to some destination (someone or
    something)."""
    Atlas = Schema(schema_storage["Atlas"])
    """A collection or bound volume of maps, charts, plates or tables, physical or in
    media form illustrating any subject."""
    Attorney = Schema(schema_storage["Attorney"])
    """Professional service: Attorney. <br/><br/>

This type is deprecated - <a class="localLink" href="#sc.LegalService">LegalService</a> is more inclusive and less ambiguous."""
    Audience = Schema(schema_storage["Audience"])
    """Intended audience for an item, i.e. the group for whom the item was created."""
    AudioObject = Schema(schema_storage["AudioObject"])
    """An audio file."""
    Audiobook = Schema(schema_storage["Audiobook"])
    """An audiobook."""
    AudiobookFormat = Schema(schema_storage["AudiobookFormat"])
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties."""
    AuthoritativeLegalValue = Schema(schema_storage["AuthoritativeLegalValue"])
    """Indicates that the publisher gives some special status to the publication of the
    document.

    ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications). Something "Authoritative" is considered to be also <a class="localLink" href="#sc.OfficialLegalValue">OfficialLegalValue</a>".
    """
    AuthorizeAction = Schema(schema_storage["AuthorizeAction"])
    """The act of granting permission to an object."""
    AutoBodyShop = Schema(schema_storage["AutoBodyShop"])
    """Auto body shop."""
    AutoDealer = Schema(schema_storage["AutoDealer"])
    """An car dealership."""
    AutoPartsStore = Schema(schema_storage["AutoPartsStore"])
    """An auto parts store."""
    AutoRental = Schema(schema_storage["AutoRental"])
    """A car rental business."""
    AutoRepair = Schema(schema_storage["AutoRepair"])
    """Car repair business."""
    AutoWash = Schema(schema_storage["AutoWash"])
    """A car wash business."""
    AutomatedTeller = Schema(schema_storage["AutomatedTeller"])
    """ATM/cash machine."""
    AutomotiveBusiness = Schema(schema_storage["AutomotiveBusiness"])
    """Car repair, sales, or parts."""
    Ayurvedic = Schema(schema_storage["Ayurvedic"])
    """A system of medicine that originated in India over thousands of years and that
    focuses on integrating and balancing the body, mind, and spirit."""
    BackOrder = Schema(schema_storage["BackOrder"])
    """Indicates that the item is available on back order."""
    BackgroundNewsArticle = Schema(schema_storage["BackgroundNewsArticle"])
    """A <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> providing
    historical context, definition and detail on a specific topic (aka "explainer" or
    "backgrounder").

    For example, an in-depth article or frequently-asked-questions (<a href
    "https://en.wikipedia.org/wiki/FAQ">FAQ</a>)
    document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using <a class="localLink" href="#sc.Book">Book</a> or <a class="localLink" href="#sc.Article">Article</a>, in particular <a class="localLink" href="#sc.ScholarlyArticle">ScholarlyArticle</a>. See also <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> for related vocabulary from a learning/education perspective.
    """
    Bacteria = Schema(schema_storage["Bacteria"])
    """Pathogenic bacteria that cause bacterial infection."""
    Bakery = Schema(schema_storage["Bakery"])
    """A bakery."""
    Balance = Schema(schema_storage["Balance"])
    """Physical activity that is engaged to help maintain posture and balance."""
    BankAccount = Schema(schema_storage["BankAccount"])
    """A product or service offered by a bank whereby one may deposit, withdraw or
    transfer money and in some cases be paid interest."""
    BankOrCreditUnion = Schema(schema_storage["BankOrCreditUnion"])
    """Bank or credit union."""
    BarOrPub = Schema(schema_storage["BarOrPub"])
    """A bar or pub."""
    Barcode = Schema(schema_storage["Barcode"])
    """An image of a visual machine-readable code such as a barcode or QR code."""
    BasicIncome = Schema(schema_storage["BasicIncome"])
    """BasicIncome: this is a benefit for basic income."""
    Beach = Schema(schema_storage["Beach"])
    """Beach."""
    BeautySalon = Schema(schema_storage["BeautySalon"])
    """Beauty salon."""
    BedAndBreakfast = Schema(schema_storage["BedAndBreakfast"])
    """Bed and breakfast.

    <br /><br /> See also the <a href="/docs/hotels.html">dedicated document on the use
    of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    BedDetails = Schema(schema_storage["BedDetails"])
    """An entity holding detailed information about the available bed types, e.g. the
    quantity of twin beds for a hotel room.

    For the single case of just one bed of a certain type, you can use bed directly with
    a text. See also <a class="localLink" href="#sc.BedType">BedType</a> (under
    development).
    """
    BedType = Schema(schema_storage["BedType"])
    """A type of bed.

    This is used for indicating the bed or beds available in an accommodation.
    """
    BefriendAction = Schema(schema_storage["BefriendAction"])
    """The act of forming a personal connection with someone (object)
    mutually/bidirectionally/symmetrically.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.FollowAction">FollowAction</a>: Unlike
    FollowAction, BefriendAction implies that the connection is reciprocal.</li> </ul>
    """
    BenefitsHealthAspect = Schema(schema_storage["BenefitsHealthAspect"])
    """Content about the benefits and advantages of usage or utilization of topic."""
    BikeStore = Schema(schema_storage["BikeStore"])
    """A bike store."""
    Blog = Schema(schema_storage["Blog"])
    """A blog."""
    BlogPosting = Schema(schema_storage["BlogPosting"])
    """A blog post."""
    BloodTest = Schema(schema_storage["BloodTest"])
    """A medical test performed on a sample of a patient's blood."""
    BoardingPolicyType = Schema(schema_storage["BoardingPolicyType"])
    """A type of boarding policy used by an airline."""
    BoatReservation = Schema(schema_storage["BoatReservation"])
    """A reservation for boat travel.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    BoatTerminal = Schema(schema_storage["BoatTerminal"])
    """A terminal for boats, ships, and other water vessels."""
    BoatTrip = Schema(schema_storage["BoatTrip"])
    """A trip on a commercial ferry line."""
    BodyMeasurementArm = Schema(schema_storage["BodyMeasurementArm"])
    """Arm length (measured between arms/shoulder line intersection and the prominent
    wrist bone).

    Used, for example, to fit shirts.
    """
    BodyMeasurementBust = Schema(schema_storage["BodyMeasurementBust"])
    """Maximum girth of bust.

    Used, for example, to fit women's suits.
    """
    BodyMeasurementChest = Schema(schema_storage["BodyMeasurementChest"])
    """Maximum girth of chest.

    Used, for example, to fit men's suits.
    """
    BodyMeasurementFoot = Schema(schema_storage["BodyMeasurementFoot"])
    """Foot length (measured between end of the most prominent toe and the most
    prominent part of the heel).

    Used, for example, to measure socks.
    """
    BodyMeasurementHand = Schema(schema_storage["BodyMeasurementHand"])
    """Maximum hand girth (measured over the knuckles of the open right hand excluding
    thumb, fingers together).

    Used, for example, to fit gloves.
    """
    BodyMeasurementHead = Schema(schema_storage["BodyMeasurementHead"])
    """Maximum girth of head above the ears.

    Used, for example, to fit hats.
    """
    BodyMeasurementHeight = Schema(schema_storage["BodyMeasurementHeight"])
    """Body height (measured between crown of head and soles of feet).

    Used, for example, to fit jackets.
    """
    BodyMeasurementHips = Schema(schema_storage["BodyMeasurementHips"])
    """Girth of hips (measured around the buttocks).

    Used, for example, to fit skirts.
    """
    BodyMeasurementInsideLeg = Schema(schema_storage["BodyMeasurementInsideLeg"])
    """Inside leg (measured between crotch and soles of feet).

    Used, for example, to fit pants.
    """
    BodyMeasurementNeck = Schema(schema_storage["BodyMeasurementNeck"])
    """Girth of neck.

    Used, for example, to fit shirts.
    """
    BodyMeasurementTypeEnumeration = Schema(
        schema_storage["BodyMeasurementTypeEnumeration"]
    )
    """Enumerates types (or dimensions) of a person's body measurements, for example for
    fitting of clothes."""
    BodyMeasurementUnderbust = Schema(schema_storage["BodyMeasurementUnderbust"])
    """Girth of body just below the bust.

    Used, for example, to fit women's swimwear.
    """
    BodyMeasurementWaist = Schema(schema_storage["BodyMeasurementWaist"])
    """Girth of natural waistline (between hip bones and lower ribs).

    Used, for example, to fit pants.
    """
    BodyMeasurementWeight = Schema(schema_storage["BodyMeasurementWeight"])
    """Body weight.

    Used, for example, to measure pantyhose.
    """
    BodyOfWater = Schema(schema_storage["BodyOfWater"])
    """A body of water, such as a sea, ocean, or lake."""
    Bone = Schema(schema_storage["Bone"])
    """Rigid connective tissue that comprises up the skeletal structure of the human
    body."""
    Book = Schema(schema_storage["Book"])
    """A book."""
    BookFormatType = Schema(schema_storage["BookFormatType"])
    """The publication format of the book."""
    BookSeries = Schema(schema_storage["BookSeries"])
    """A series of books.

    Included books can be indicated with the hasPart property.
    """
    BookStore = Schema(schema_storage["BookStore"])
    """A bookstore."""
    BookmarkAction = Schema(schema_storage["BookmarkAction"])
    """An agent bookmarks/flags/labels/tags/marks an object."""
    Boolean = Schema(schema_storage["Boolean"])
    """Boolean: True or False."""
    BorrowAction = Schema(schema_storage["BorrowAction"])
    """The act of obtaining an object under an agreement to return it at a later date.
    Reciprocal of LendAction.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.LendAction">LendAction</a>: Reciprocal of
    BorrowAction.</li> </ul>
    """
    BowlingAlley = Schema(schema_storage["BowlingAlley"])
    """A bowling alley."""
    BrainStructure = Schema(schema_storage["BrainStructure"])
    """Any anatomical structure which pertains to the soft nervous tissue functioning as
    the coordinating center of sensation and intellectual and nervous activity."""
    Brand = Schema(schema_storage["Brand"])
    """A brand is a name used by an organization or business person for labeling a
    product, product group, or similar."""
    BreadcrumbList = Schema(schema_storage["BreadcrumbList"])
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages,
    typically described using at least their URL and their name, and typically ending
    with the current page.<br/><br/>

    The <a class="localLink" href="#sc.position">position</a> property is used to reconstruct the order of the items in a BreadcrumbList The convention is that a breadcrumb list has an <a class="localLink" href="#sc.itemListOrder">itemListOrder</a> of <a class="localLink" href="#sc.ItemListOrderAscending">ItemListOrderAscending</a> (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.
    """
    Brewery = Schema(schema_storage["Brewery"])
    """Brewery."""
    Bridge = Schema(schema_storage["Bridge"])
    """A bridge."""
    BroadcastChannel = Schema(schema_storage["BroadcastChannel"])
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup."""
    BroadcastEvent = Schema(schema_storage["BroadcastEvent"])
    """An over the air or online broadcast event."""
    BroadcastFrequencySpecification = Schema(
        schema_storage["BroadcastFrequencySpecification"]
    )
    """The frequency in MHz and the modulation used for a particular
    BroadcastService."""
    BroadcastRelease = Schema(schema_storage["BroadcastRelease"])
    """BroadcastRelease."""
    BroadcastService = Schema(schema_storage["BroadcastService"])
    """A delivery service through which content is provided via broadcast over the air
    or online."""
    BrokerageAccount = Schema(schema_storage["BrokerageAccount"])
    """An account that allows an investor to deposit funds and place investment orders
    with a licensed broker or brokerage firm."""
    BuddhistTemple = Schema(schema_storage["BuddhistTemple"])
    """A Buddhist temple."""
    BusOrCoach = Schema(schema_storage["BusOrCoach"])
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers.

    Coaches are luxury busses, usually in service for long distance travel.
    """
    BusReservation = Schema(schema_storage["BusReservation"])
    """A reservation for bus travel. <br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    BusStation = Schema(schema_storage["BusStation"])
    """A bus station."""
    BusStop = Schema(schema_storage["BusStop"])
    """A bus stop."""
    BusTrip = Schema(schema_storage["BusTrip"])
    """A trip on a commercial bus line."""
    BusinessAudience = Schema(schema_storage["BusinessAudience"])
    """A set of characteristics belonging to businesses, e.g. who compose an item's
    target audience."""
    BusinessEntityType = Schema(schema_storage["BusinessEntityType"])
    """A business entity type is a conceptual entity representing the legal form, the
    size, the main line of business, the position in the value chain, or any combination
    thereof, of an organization or business person.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#Business</li>
    <li>http://purl.org/goodrelations/v1#Enduser</li>
    <li>http://purl.org/goodrelations/v1#PublicInstitution</li>
    <li>http://purl.org/goodrelations/v1#Reseller</li>
    </ul>
    """
    BusinessEvent = Schema(schema_storage["BusinessEvent"])
    """Event type: Business event."""
    BusinessFunction = Schema(schema_storage["BusinessFunction"])
    """The business function specifies the type of activity or access (i.e., the bundle
    of rights) offered by the organization or business person through the offer. Typical
    are sell, rental or lease, maintenance or repair, manufacture / produce, recycle /
    dispose, engineering / construction, or installation. Proprietary specifications of
    access rights are also instances of this class.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#ConstructionInstallation</li>
    <li>http://purl.org/goodrelations/v1#Dispose</li>
    <li>http://purl.org/goodrelations/v1#LeaseOut</li>
    <li>http://purl.org/goodrelations/v1#Maintain</li>
    <li>http://purl.org/goodrelations/v1#ProvideService</li>
    <li>http://purl.org/goodrelations/v1#Repair</li>
    <li>http://purl.org/goodrelations/v1#Sell</li>
    <li>http://purl.org/goodrelations/v1#Buy</li>
    </ul>
    """
    BusinessSupport = Schema(schema_storage["BusinessSupport"])
    """BusinessSupport: this is a benefit for supporting businesses."""
    BuyAction = Schema(schema_storage["BuyAction"])
    """The act of giving money to a seller in exchange for goods or services rendered.

    An agent buys an object, product, or service from a seller for a price. Reciprocal
    of SellAction.
    """
    CDCPMDRecord = Schema(schema_storage["CDCPMDRecord"])
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data
    format used for hospital data reporting.

    See <a href="/docs/cdc-covid.html">documentation</a> for details, and the linked CDC
    materials for authoritative definitions used as the source here.
    """
    CDFormat = Schema(schema_storage["CDFormat"])
    """CDFormat."""
    CT = Schema(schema_storage["CT"])
    """X-ray computed tomography imaging."""
    CableOrSatelliteService = Schema(schema_storage["CableOrSatelliteService"])
    """A service which provides access to media programming like TV or radio.

    Access may be via cable or satellite.
    """
    CafeOrCoffeeShop = Schema(schema_storage["CafeOrCoffeeShop"])
    """A cafe or coffee shop."""
    Campground = Schema(schema_storage["Campground"])
    """A camping site, campsite, or <a class="localLink"
    href="#sc.Campground">Campground</a> is a place used for overnight stay in the
    outdoors, typically containing individual <a class="localLink"
    href="#sc.CampingPitch">CampingPitch</a> locations. <br/><br/>

    In British English a campsite is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites (Source: Wikipedia see <a href="https://en.wikipedia.org/wiki/Campsite">https://en.wikipedia.org/wiki/Campsite</a>).<br/><br/>

    See also the dedicated <a href="/docs/hotels.html">document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    CampingPitch = Schema(schema_storage["CampingPitch"])
    """A <a class="localLink" href="#sc.CampingPitch">CampingPitch</a> is an individual
    place for overnight stay in the outdoors, typically being part of a larger camping
    site, or <a class="localLink" href="#sc.Campground">Campground</a>.<br/><br/>

    In British English a campsite, or campground, is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites.
    (Source: Wikipedia see <a href="https://en.wikipedia.org/wiki/Campsite">https://en.wikipedia.org/wiki/Campsite</a>).<br/><br/>

    See also the dedicated <a href="/docs/hotels.html">document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    Canal = Schema(schema_storage["Canal"])
    """A canal, like the Panama Canal."""
    CancelAction = Schema(schema_storage["CancelAction"])
    """The act of asserting that a future event/action is no longer going to
    happen.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ConfirmAction">ConfirmAction</a>: The
    antonym of CancelAction.</li> </ul>
    """
    Car = Schema(schema_storage["Car"])
    """A car is a wheeled, self-powered motor vehicle used for transportation."""
    CarUsageType = Schema(schema_storage["CarUsageType"])
    """A value indicating a special usage of a car, e.g. commercial rental, driving
    school, or as a taxi."""
    Cardiovascular = Schema(schema_storage["Cardiovascular"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of heart and vasculature."""
    CardiovascularExam = Schema(schema_storage["CardiovascularExam"])
    """Cardiovascular system assessment withclinical examination."""
    CaseSeries = Schema(schema_storage["CaseSeries"])
    """A case series (also known as a clinical series) is a medical research study that
    tracks patients with a known exposure given similar treatment or examines their
    medical records for exposure and outcome.

    A case series can be retrospective or prospective and usually involves a smaller
    number of patients than the more powerful case-control studies or randomized
    controlled trials. Case series may be consecutive or non-consecutive, depending on
    whether all cases presenting to the reporting authors over a period of time were
    included, or only a selection.
    """
    Casino = Schema(schema_storage["Casino"])
    """A casino."""
    CassetteFormat = Schema(schema_storage["CassetteFormat"])
    """CassetteFormat."""
    CategoryCode = Schema(schema_storage["CategoryCode"])
    """A Category Code."""
    CategoryCodeSet = Schema(schema_storage["CategoryCodeSet"])
    """A set of Category Code values."""
    CatholicChurch = Schema(schema_storage["CatholicChurch"])
    """A Catholic church."""
    CausesHealthAspect = Schema(schema_storage["CausesHealthAspect"])
    """Information about the causes and main actions that gave rise to the topic."""
    Cemetery = Schema(schema_storage["Cemetery"])
    """A graveyard."""
    Chapter = Schema(schema_storage["Chapter"])
    """One of the sections into which a book is divided.

    A chapter usually has a section number or a name.
    """
    CharitableIncorporatedOrganization = Schema(
        schema_storage["CharitableIncorporatedOrganization"]
    )
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK)."""
    CheckAction = Schema(schema_storage["CheckAction"])
    """An agent inspects, determines, investigates, inquires, or examines an object's
    accuracy, quality, condition, or state."""
    CheckInAction = Schema(schema_storage["CheckInAction"])
    """The act of an agent communicating (service provider, social media, etc) their
    arrival by registering/confirming for a previously reserved service (e.g. flight
    check in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass,
    etc).<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.CheckOutAction">CheckOutAction</a>: The
    antonym of CheckInAction.</li> <li><a class="localLink"
    href="#sc.ArriveAction">ArriveAction</a>: Unlike ArriveAction, CheckInAction implies
    that the agent is informing/confirming the start of a previously reserved
    service.</li> <li><a class="localLink" href="#sc.ConfirmAction">ConfirmAction</a>:
    Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming
    the <em>start</em> of a previously reserved service rather than its
    validity/existence.</li> </ul>
    """
    CheckOutAction = Schema(schema_storage["CheckOutAction"])
    """The act of an agent communicating (service provider, social media, etc) their
    departure of a previously reserved service (e.g. flight check in) or place (e.g.
    hotel).<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.CheckInAction">CheckInAction</a>: The
    antonym of CheckOutAction.</li> <li><a class="localLink"
    href="#sc.DepartAction">DepartAction</a>: Unlike DepartAction, CheckOutAction
    implies that the agent is informing/confirming the end of a previously reserved
    service.</li> <li><a class="localLink" href="#sc.CancelAction">CancelAction</a>:
    Unlike CancelAction, CheckOutAction implies that the agent is informing/confirming
    the end of a previously reserved service.</li> </ul>
    """
    CheckoutPage = Schema(schema_storage["CheckoutPage"])
    """Web page type: Checkout page."""
    ChildCare = Schema(schema_storage["ChildCare"])
    """A Childcare center."""
    ChildrensEvent = Schema(schema_storage["ChildrensEvent"])
    """Event type: Children's event."""
    Chiropractic = Schema(schema_storage["Chiropractic"])
    """A system of medicine focused on the relationship between the body's structure,
    mainly the spine, and its functioning."""
    ChooseAction = Schema(schema_storage["ChooseAction"])
    """The act of expressing a preference from a set of options or a large or unbounded
    set of choices/options."""
    Church = Schema(schema_storage["Church"])
    """A church."""
    City = Schema(schema_storage["City"])
    """A city or town."""
    CityHall = Schema(schema_storage["CityHall"])
    """A city hall."""
    CivicStructure = Schema(schema_storage["CivicStructure"])
    """A public structure, such as a town hall or concert hall."""
    Claim = Schema(schema_storage["Claim"])
    """A <a class="localLink" href="#sc.Claim">Claim</a> in Schema.org represents a
    specific, factually-oriented claim that could be the <a class="localLink"
    href="#sc.itemReviewed">itemReviewed</a> in a <a class="localLink"
    href="#sc.ClaimReview">ClaimReview</a>. The content of a claim can be summarized
    with the <a class="localLink" href="#sc.text">text</a> property. Variations on well
    known claims can have their common identity indicated via <a class="localLink"
    href="#sc.sameAs">sameAs</a> links, and summarized with a <a class="localLink"
    href="#sc.name">name</a>. Ideally, a <a class="localLink" href="#sc.Claim">Claim</a>
    description includes enough contextual information to minimize the risk of ambiguity
    or inclarity. In practice, many claims are better understood in the context in which
    they appear or the interpretations provided by claim reviews.<br/><br/>

    Beyond <a class="localLink" href="#sc.ClaimReview">ClaimReview</a>, the Claim type can be associated with related creative works - for example a <a class="localLink" href="#sc.ScholarlyArticle">ScholarlyArticle</a> or <a class="localLink" href="#sc.Question">Question</a> might be <a class="localLink" href="#sc.about">about</a> some <a class="localLink" href="#sc.Claim">Claim</a>.<br/><br/>

    At this time, Schema.org does not define any types of relationship between claims. This is a natural area for future exploration.
    """
    ClaimReview = Schema(schema_storage["ClaimReview"])
    """A fact-checking review of claims made (or reported) in some creative work
    (referenced via itemReviewed)."""
    Class = Schema(schema_storage["Class"])
    """A class, also often called a 'Type'; equivalent to rdfs:Class."""
    CleaningFee = Schema(schema_storage["CleaningFee"])
    """Represents the cleaning fee part of the total price for an offered product, for
    example a vacation rental."""
    Clinician = Schema(schema_storage["Clinician"])
    """Medical clinicians, including practicing physicians and other medical
    professionals involved in clinical practice."""
    Clip = Schema(schema_storage["Clip"])
    """A short TV or radio program or a segment/part of a program."""
    ClothingStore = Schema(schema_storage["ClothingStore"])
    """A clothing store."""
    CoOp = Schema(schema_storage["CoOp"])
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends."""
    Code = Schema(schema_storage["Code"])
    """Computer programming source code.

    Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    CohortStudy = Schema(schema_storage["CohortStudy"])
    """Also known as a panel study.

    A cohort study is a form of longitudinal study used in medicine and social science.
    It is one type of study design and should be compared with a cross-sectional study.
    A cohort is a group of people who share a common characteristic or experience within
    a defined period (e.g., are born, leave school, lose their job, are exposed to a
    drug or a vaccine, etc.). The comparison group may be the general population from
    which the cohort is drawn, or it may be another cohort of persons thought to have
    had little or no exposure to the substance under investigation, but otherwise
    similar. Alternatively, subgroups within the cohort may be compared with each other.
    """
    Collection = Schema(schema_storage["Collection"])
    """A collection of items e.g. creative works or products."""
    CollectionPage = Schema(schema_storage["CollectionPage"])
    """Web page type: Collection page."""
    CollegeOrUniversity = Schema(schema_storage["CollegeOrUniversity"])
    """A college, university, or other third-level educational institution."""
    ComedyClub = Schema(schema_storage["ComedyClub"])
    """A comedy club."""
    ComedyEvent = Schema(schema_storage["ComedyEvent"])
    """Event type: Comedy event."""
    ComicCoverArt = Schema(schema_storage["ComicCoverArt"])
    """The artwork on the cover of a comic."""
    ComicIssue = Schema(schema_storage["ComicIssue"])
    """Individual comic issues are serially published as part of a larger series.

    For the sake of consistency, even one-shot issues
    belong to a series comprised of a single issue. All comic issues can be
    uniquely identified by: the combination of the name and volume number of the
    series to which the issue belongs; the issue number; and the variant
    description of the issue (if any).
    """
    ComicSeries = Schema(schema_storage["ComicSeries"])
    """A sequential publication of comic stories under a unifying title, for example
    "The Amazing Spider-Man" or "Groo the Wanderer"."""
    ComicStory = Schema(schema_storage["ComicStory"])
    """The term "story" is any indivisible, re-printable unit of a comic, including the
    interior stories, covers, and backmatter.

    Most
    comics have at least two stories: a cover (ComicCoverArt) and an interior story.
    """
    Comment = Schema(schema_storage["Comment"])
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the <a class="localLink" href="#sc.text">text</a> property, and its topic via <a class="localLink" href="#sc.about">about</a>, properties shared with all CreativeWorks."""
    CommentAction = Schema(schema_storage["CommentAction"])
    """The act of generating a comment about a subject."""
    CommentPermission = Schema(schema_storage["CommentPermission"])
    """Permission to add comments to the document."""
    CommunicateAction = Schema(schema_storage["CommunicateAction"])
    """The act of conveying information to another person via a communication medium
    (instrument) such as speech, email, or telephone conversation."""
    CommunityHealth = Schema(schema_storage["CommunityHealth"])
    """A field of public health focusing on improving health characteristics of a
    defined population in relation with their geographical or environment areas."""
    CompilationAlbum = Schema(schema_storage["CompilationAlbum"])
    """CompilationAlbum."""
    CompleteDataFeed = Schema(schema_storage["CompleteDataFeed"])
    """A <a class="localLink" href="#sc.CompleteDataFeed">CompleteDataFeed</a> is a <a
    class="localLink" href="#sc.DataFeed">DataFeed</a> whose standard representation
    includes content for every item currently in the feed.<br/><br/>

    This is the equivalent of Atom's element as defined in Feed Paging and Archiving <a
    href="
    https://tools.ietf.org/html/rfc5005">RFC
    5005</a>, For example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items.
    """
    Completed = Schema(schema_storage["Completed"])
    """Completed."""
    CompletedActionStatus = Schema(schema_storage["CompletedActionStatus"])
    """An action that has already taken place."""
    CompoundPriceSpecification = Schema(schema_storage["CompoundPriceSpecification"])
    """A compound price specification is one that bundles multiple prices that all apply
    in combination for different dimensions of consumption.

    Use the name property of the attached unit price specification for indicating the
    dimension of a price component (e.g. "electricity" or "final cleaning").
    """
    ComputerLanguage = Schema(schema_storage["ComputerLanguage"])
    """This type covers computer programming languages such as Scheme and Lisp, as well
    as other language-like computer representations.

    Natural languages are best represented with the <a class="localLink"
    href="#sc.Language">Language</a> type.
    """
    ComputerStore = Schema(schema_storage["ComputerStore"])
    """A computer store."""
    ConfirmAction = Schema(schema_storage["ConfirmAction"])
    """The act of notifying someone that a future event/action is going to happen as
    expected.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.CancelAction">CancelAction</a>: The antonym
    of ConfirmAction.</li> </ul>
    """
    Consortium = Schema(schema_storage["Consortium"])
    """A Consortium is a membership <a class="localLink"
    href="#sc.Organization">Organization</a> whose members are typically
    Organizations."""
    ConsumeAction = Schema(schema_storage["ConsumeAction"])
    """The act of ingesting information/resources/food."""
    ContactPage = Schema(schema_storage["ContactPage"])
    """Web page type: Contact page."""
    ContactPoint = Schema(schema_storage["ContactPoint"])
    """A contact point&#x2014;for example, a Customer Complaints department."""
    ContactPointOption = Schema(schema_storage["ContactPointOption"])
    """Enumerated options related to a ContactPoint."""
    ContagiousnessHealthAspect = Schema(schema_storage["ContagiousnessHealthAspect"])
    """Content about contagion mechanisms and contagiousness information over the
    topic."""
    Continent = Schema(schema_storage["Continent"])
    """One of the continents (for example, Europe or Africa)."""
    ControlAction = Schema(schema_storage["ControlAction"])
    """An agent controls a device or application."""
    ConvenienceStore = Schema(schema_storage["ConvenienceStore"])
    """A convenience store."""
    Conversation = Schema(schema_storage["Conversation"])
    """One or more messages between organizations or people on a particular topic.

    Individual messages can be linked to the conversation with isPartOf or hasPart
    properties.
    """
    CookAction = Schema(schema_storage["CookAction"])
    """The act of producing/preparing food."""
    Corporation = Schema(schema_storage["Corporation"])
    """Organization: A business corporation."""
    CorrectionComment = Schema(schema_storage["CorrectionComment"])
    """A <a class="localLink" href="#sc.comment">comment</a> that corrects <a
    class="localLink" href="#sc.CreativeWork">CreativeWork</a>."""
    Country = Schema(schema_storage["Country"])
    """A country."""
    Course = Schema(schema_storage["Course"])
    """A description of an educational course which may be offered as distinct instances
    at which take place at different times or take place at different locations, or be
    offered through different media or modes of study.

    An educational course is a sequence of one or more educational events and/or
    creative works which aims to build knowledge, competence or ability of learners.
    """
    CourseInstance = Schema(schema_storage["CourseInstance"])
    """An instance of a <a class="localLink" href="#sc.Course">Course</a> which is
    distinct from other instances because it is offered at a different time or location
    or through different media or modes of study or to a specific section of
    students."""
    Courthouse = Schema(schema_storage["Courthouse"])
    """A courthouse."""
    CoverArt = Schema(schema_storage["CoverArt"])
    """The artwork on the outer surface of a CreativeWork."""
    CovidTestingFacility = Schema(schema_storage["CovidTestingFacility"])
    """A CovidTestingFacility is a <a class="localLink"
    href="#sc.MedicalClinic">MedicalClinic</a> where testing for the COVID-19
    Coronavirus disease is available.

    If the facility is being made available from an established <a class="localLink"
    href="#sc.Pharmacy">Pharmacy</a>, <a class="localLink" href="#sc.Hotel">Hotel</a>,
    or other non-medical organization, multiple types can be listed. This makes it
    easier to re-use existing schema.org information about that place e.g. contact info,
    address, opening hours. Note that in an emergency, such information may not always
    be reliable.
    """
    CreateAction = Schema(schema_storage["CreateAction"])
    """The act of deliberately creating/producing/generating/building a result out of
    the agent."""
    CreativeWork = Schema(schema_storage["CreativeWork"])
    """The most generic kind of creative work, including books, movies, photographs,
    software programs, etc."""
    CreativeWorkSeason = Schema(schema_storage["CreativeWorkSeason"])
    """A media season e.g. tv, radio, video game etc."""
    CreativeWorkSeries = Schema(schema_storage["CreativeWorkSeries"])
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not
    necessarily of the same kind. CreativeWorkSeries are usually organized into some
    order, often chronological. Unlike <a class="localLink"
    href="#sc.ItemList">ItemList</a> which is a general purpose data structure for lists
    of things, the emphasis with CreativeWorkSeries is on published materials (written
    e.g. books and periodicals, or media such as tv, radio and games).<br/><br/>

    Specific subtypes are available for describing <a class="localLink"
    href="#sc.TVSeries">TVSeries</a>, <a class="localLink"
    href="#sc.RadioSeries">RadioSeries</a>, <a class="localLink"
    href="#sc.MovieSeries">MovieSeries</a>, <a class="localLink"
    href="#sc.BookSeries">BookSeries</a>, <a class="localLink"
    href="#sc.Periodical">Periodical</a> and <a class="localLink"
    href="#sc.VideoGameSeries">VideoGameSeries</a>. In each case, the <a
    class="localLink" href="#sc.hasPart">hasPart</a> / <a class="localLink"
    href="#sc.isPartOf">isPartOf</a> properties can be used to relate the
    CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
    just to organize these more specific and practical subtypes.<br/><br/>

    It is common for properties applicable to an item from the series to be usefully
    applied to the containing group. Schema.org attempts to anticipate some of these
    cases, but publishers should be free to apply properties of the series parts to the
    series as a whole wherever they seem appropriate.
    """
    CreditCard = Schema(schema_storage["CreditCard"])
    """A card payment method of a particular brand or name.  Used to mark up a
    particular payment method and/or the financial product/service that supplies the
    card account.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#AmericanExpress</li>
    <li>http://purl.org/goodrelations/v1#DinersClub</li>
    <li>http://purl.org/goodrelations/v1#Discover</li>
    <li>http://purl.org/goodrelations/v1#JCB</li>
    <li>http://purl.org/goodrelations/v1#MasterCard</li>
    <li>http://purl.org/goodrelations/v1#VISA</li>
    </ul>
    """
    Crematorium = Schema(schema_storage["Crematorium"])
    """A crematorium."""
    CriticReview = Schema(schema_storage["CriticReview"])
    """A <a class="localLink" href="#sc.CriticReview">CriticReview</a> is a more
    specialized form of Review written or published by a source that is recognized for
    its reviewing activities.

    These can include online columns, travel and food guides, TV and radio shows, blogs
    and other independent Web sites. <a class="localLink"
    href="#sc.CriticReview">CriticReview</a>s are typically more in-depth and
    professionally written. For simpler, casually written user/visitor/viewer/customer
    reviews, it is more appropriate to use the <a class="localLink"
    href="#sc.UserReview">UserReview</a> type. Review aggregator sites such as
    Metacritic already separate out the site's user reviews from selected critic reviews
    that originate from third-party sources.
    """
    CrossSectional = Schema(schema_storage["CrossSectional"])
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such
    as that collected by the Census Bureau.

    Sometimes called Prevalence Studies.
    """
    CssSelectorType = Schema(schema_storage["CssSelectorType"])
    """Text representing a CSS selector."""
    CurrencyConversionService = Schema(schema_storage["CurrencyConversionService"])
    """A service to convert funds from one currency to another currency."""
    DDxElement = Schema(schema_storage["DDxElement"])
    """An alternative, closely-related condition typically considered later in the
    differential diagnosis process along with the signs that are used to distinguish
    it."""
    DJMixAlbum = Schema(schema_storage["DJMixAlbum"])
    """DJMixAlbum."""
    DVDFormat = Schema(schema_storage["DVDFormat"])
    """DVDFormat."""
    DamagedCondition = Schema(schema_storage["DamagedCondition"])
    """Indicates that the item is damaged."""
    DanceEvent = Schema(schema_storage["DanceEvent"])
    """Event type: A social dance."""
    DanceGroup = Schema(schema_storage["DanceGroup"])
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance."""
    DataCatalog = Schema(schema_storage["DataCatalog"])
    """A collection of datasets."""
    DataDownload = Schema(schema_storage["DataDownload"])
    """A dataset in downloadable form."""
    DataFeed = Schema(schema_storage["DataFeed"])
    """A single feed providing structured information about one or more entities or
    topics."""
    DataFeedItem = Schema(schema_storage["DataFeedItem"])
    """A single item within a larger data feed."""
    DataType = Schema(schema_storage["DataType"])
    """The basic data types such as Integers, Strings, etc."""
    Dataset = Schema(schema_storage["Dataset"])
    """A body of structured information describing some topic(s) of interest."""
    Date = Schema(schema_storage["Date"])
    """A date value in <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO 8601 date format</a>."""
    DateTime = Schema(schema_storage["DateTime"])
    """A combination of date and time of day in the form [-]CCYY-MM-
    DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601)."""
    DatedMoneySpecification = Schema(schema_storage["DatedMoneySpecification"])
    """A DatedMoneySpecification represents monetary values with optional start and end
    dates.

    For example, this could represent an employee's salary over a specific period of
    time. <strong>Note:</strong> This type has been superseded by <a class="localLink"
    href="#sc.MonetaryAmount">MonetaryAmount</a> use of that type is recommended
    """
    DayOfWeek = Schema(schema_storage["DayOfWeek"])
    """The day of the week, e.g. used to specify to which day the opening hours of an
    OpeningHoursSpecification refer.<br/><br/>

    Originally, URLs from <a href="http://purl.org/goodrelations/v1">GoodRelations</a> were used (for <a class="localLink" href="#sc.Monday">Monday</a>, <a class="localLink" href="#sc.Tuesday">Tuesday</a>, <a class="localLink" href="#sc.Wednesday">Wednesday</a>, <a class="localLink" href="#sc.Thursday">Thursday</a>, <a class="localLink" href="#sc.Friday">Friday</a>, <a class="localLink" href="#sc.Saturday">Saturday</a>, <a class="localLink" href="#sc.Sunday">Sunday</a> plus a special entry for <a class="localLink" href="#sc.PublicHolidays">PublicHolidays</a>); these have now been integrated directly into schema.org.
    """
    DaySpa = Schema(schema_storage["DaySpa"])
    """A day spa."""
    DeactivateAction = Schema(schema_storage["DeactivateAction"])
    """The act of stopping or deactivating a device or application (e.g. stopping a
    timer or turning off a flashlight)."""
    DecontextualizedContent = Schema(schema_storage["DecontextualizedContent"])
    """Content coded 'missing context' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'missing
    context': Presenting unaltered video in an inaccurate manner that misrepresents the
    footage. For example, using incorrect dates or locations, altering the transcript or
    sharing brief clips from a longer video to mislead viewers. (A video rated
    'original' can also be missing context.)<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be 'missing
    context': Presenting unaltered images in an inaccurate manner to misrepresent the
    image and mislead the viewer. For example, a common tactic is using an unaltered
    image but saying it came from a different time or place. (An image rated 'original'
    can also be missing context.)<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'missing context': An unaltered image presented in an inaccurate manner
    to misrepresent the image and mislead the viewer. For example, a common tactic is
    using an unaltered image but saying it came from a different time or place. (An
    'original' image with inaccurate text would generally fall in this
    category.)<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be 'missing
    context': Unaltered audio presented in an inaccurate manner that misrepresents it.
    For example, using incorrect dates or locations, or sharing brief clips from a
    longer recording to mislead viewers. (Audio rated “original” can also be missing
    context.)
    """
    DefenceEstablishment = Schema(schema_storage["DefenceEstablishment"])
    """A defence establishment, such as an army or navy base."""
    DefinedRegion = Schema(schema_storage["DefinedRegion"])
    """A DefinedRegion is a geographic area defined by potentially arbitrary (rather
    than political, administrative or natural geographical) criteria. Properties are
    provided for defining a region by reference to sets of postal codes.<br/><br/>

    Examples: a delivery destination when shopping. Region where regional pricing is configured.<br/><br/>

    Requirement 1:
    Country: US
    States: "NY", "CA"<br/><br/>

    Requirement 2:
    Country: US
    PostalCode Set: { [94000-94585], [97000, 97999], [13000, 13599]}
    { [12345, 12345], [78945, 78945], }
    Region = state, canton, prefecture, autonomous community...
    """
    DefinedTerm = Schema(schema_storage["DefinedTerm"])
    """A word, name, acronym, phrase, etc.

    with a formal definition. Often used in the context of category or subject
    classification, glossaries or dictionaries, product or creative work types, etc. Use
    the name property for the term being defined, use termCode if the term has an alpha-
    numeric code allocated, use description to provide the definition of the term.
    """
    DefinedTermSet = Schema(schema_storage["DefinedTermSet"])
    """A set of defined terms for example a set of categories or a classification
    scheme, a glossary, dictionary or enumeration."""
    DefinitiveLegalValue = Schema(schema_storage["DefinitiveLegalValue"])
    """Indicates a document for which the text is conclusively what the law says and is
    legally binding.

    (e.g. The digitally signed version of an Official Journal.)
    Something "Definitive" is considered to be also <a class="localLink" href="#sc.AuthoritativeLegalValue">AuthoritativeLegalValue</a>.
    """
    DeleteAction = Schema(schema_storage["DeleteAction"])
    """The act of editing a recipient by removing one of its objects."""
    DeliveryChargeSpecification = Schema(schema_storage["DeliveryChargeSpecification"])
    """The price for the delivery of an offer using a particular delivery method."""
    DeliveryEvent = Schema(schema_storage["DeliveryEvent"])
    """An event involving the delivery of an item."""
    DeliveryMethod = Schema(schema_storage["DeliveryMethod"])
    """A delivery method is a standardized procedure for transferring the product or
    service to the destination of fulfillment chosen by the customer. Delivery methods
    are characterized by the means of transportation used, and by the organization or
    group that is the contracting party for the sending organization or
    person.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#DeliveryModeDirectDownload</li>
    <li>http://purl.org/goodrelations/v1#DeliveryModeFreight</li>
    <li>http://purl.org/goodrelations/v1#DeliveryModeMail</li>
    <li>http://purl.org/goodrelations/v1#DeliveryModeOwnFleet</li>
    <li>http://purl.org/goodrelations/v1#DeliveryModePickUp</li>
    <li>http://purl.org/goodrelations/v1#DHL</li>
    <li>http://purl.org/goodrelations/v1#FederalExpress</li>
    <li>http://purl.org/goodrelations/v1#UPS</li>
    </ul>
    """
    DeliveryTimeSettings = Schema(schema_storage["DeliveryTimeSettings"])
    """A DeliveryTimeSettings represents re-usable pieces of shipping information,
    relating to timing.

    It is designed for publication on an URL that may be referenced via the <a class="localLink" href="#sc.shippingSettingsLink">shippingSettingsLink</a> property of a <a class="localLink" href="#sc.OfferShippingDetails">OfferShippingDetails</a>. Several occurrences can be published, distinguished (and identified/referenced) by their different values for <a class="localLink" href="#sc.transitTimeLabel">transitTimeLabel</a>.
    """
    Demand = Schema(schema_storage["Demand"])
    """A demand entity represents the public, not necessarily binding, not necessarily
    exclusive, announcement by an organization or person to seek a certain type of goods
    or services.

    For describing demand using this type, the very same properties used for Offer
    apply.
    """
    DemoAlbum = Schema(schema_storage["DemoAlbum"])
    """DemoAlbum."""
    Dentist = Schema(schema_storage["Dentist"])
    """A dentist."""
    Dentistry = Schema(schema_storage["Dentistry"])
    """A branch of medicine that is involved in the dental care."""
    DepartAction = Schema(schema_storage["DepartAction"])
    """The act of  departing from a place.

    An agent departs from an fromLocation for a destination, optionally with
    participants.
    """
    DepartmentStore = Schema(schema_storage["DepartmentStore"])
    """A department store."""
    DepositAccount = Schema(schema_storage["DepositAccount"])
    """A type of Bank Account with a main purpose of depositing funds to gain interest
    or other benefits."""
    Dermatologic = Schema(schema_storage["Dermatologic"])
    """Something relating to or practicing dermatology."""
    Dermatology = Schema(schema_storage["Dermatology"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of skin."""
    DiabeticDiet = Schema(schema_storage["DiabeticDiet"])
    """A diet appropriate for people with diabetes."""
    Diagnostic = Schema(schema_storage["Diagnostic"])
    """A medical device used for diagnostic purposes."""
    DiagnosticLab = Schema(schema_storage["DiagnosticLab"])
    """A medical laboratory that offers on-site or off-site diagnostic services."""
    DiagnosticProcedure = Schema(schema_storage["DiagnosticProcedure"])
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic,
    purposes."""
    Diet = Schema(schema_storage["Diet"])
    """A strategy of regulating the intake of food to achieve or maintain a specific
    health-related goal."""
    DietNutrition = Schema(schema_storage["DietNutrition"])
    """Dietetic and nutrition as a medical specialty."""
    DietarySupplement = Schema(schema_storage["DietarySupplement"])
    """A product taken by mouth that contains a dietary ingredient intended to
    supplement the diet.

    Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino
    acids, and substances such as enzymes, organ tissues, glandulars and metabolites.
    """
    DigitalAudioTapeFormat = Schema(schema_storage["DigitalAudioTapeFormat"])
    """DigitalAudioTapeFormat."""
    DigitalDocument = Schema(schema_storage["DigitalDocument"])
    """An electronic file or document."""
    DigitalDocumentPermission = Schema(schema_storage["DigitalDocumentPermission"])
    """A permission for a particular person or group to access a particular file."""
    DigitalDocumentPermissionType = Schema(
        schema_storage["DigitalDocumentPermissionType"]
    )
    """A type of permission which can be granted for accessing a digital document."""
    DigitalFormat = Schema(schema_storage["DigitalFormat"])
    """DigitalFormat."""
    DisabilitySupport = Schema(schema_storage["DisabilitySupport"])
    """DisabilitySupport: this is a benefit for disability support."""
    DisagreeAction = Schema(schema_storage["DisagreeAction"])
    """The act of expressing a difference of opinion with the object.

    An agent disagrees to/about an object (a proposition, topic or theme) with
    participants.
    """
    Discontinued = Schema(schema_storage["Discontinued"])
    """Indicates that the item has been discontinued."""
    DiscoverAction = Schema(schema_storage["DiscoverAction"])
    """The act of discovering/finding an object."""
    DiscussionForumPosting = Schema(schema_storage["DiscussionForumPosting"])
    """A posting to a discussion forum."""
    DislikeAction = Schema(schema_storage["DislikeAction"])
    """The act of expressing a negative sentiment about the object.

    An agent dislikes an object (a proposition, topic or theme) with participants.
    """
    Distance = Schema(schema_storage["Distance"])
    """Properties that take Distances as values are of the form '&lt;Number&gt;
    &lt;Length unit of measure&gt;'.

    E.g., '7 ft'.
    """
    DistanceFee = Schema(schema_storage["DistanceFee"])
    """Represents the distance fee (e.g., price per km or mile) part of the total price
    for an offered product, for example a car rental."""
    Distillery = Schema(schema_storage["Distillery"])
    """A distillery."""
    DonateAction = Schema(schema_storage["DonateAction"])
    """The act of providing goods, services, or money without compensation, often for
    philanthropic reasons."""
    DoseSchedule = Schema(schema_storage["DoseSchedule"])
    """A specific dosing schedule for a drug or supplement."""
    DoubleBlindedTrial = Schema(schema_storage["DoubleBlindedTrial"])
    """A trial design in which neither the researcher nor the patient knows the details
    of the treatment the patient was randomly assigned to."""
    DownloadAction = Schema(schema_storage["DownloadAction"])
    """The act of downloading an object."""
    Downpayment = Schema(schema_storage["Downpayment"])
    """Represents the downpayment (up-front payment) price component of the total price
    for an offered product that has additional installment payments."""
    DrawAction = Schema(schema_storage["DrawAction"])
    """The act of producing a visual/graphical representation of an object, typically
    with a pen/pencil and paper as instruments."""
    Drawing = Schema(schema_storage["Drawing"])
    """A picture or diagram made with a pencil, pen, or crayon rather than paint."""
    DrinkAction = Schema(schema_storage["DrinkAction"])
    """The act of swallowing liquids."""
    DriveWheelConfigurationValue = Schema(
        schema_storage["DriveWheelConfigurationValue"]
    )
    """A value indicating which roadwheels will receive torque."""
    DrivingSchoolVehicleUsage = Schema(schema_storage["DrivingSchoolVehicleUsage"])
    """Indicates the usage of the vehicle for driving school."""
    Drug = Schema(schema_storage["Drug"])
    """A chemical or biologic substance, used as a medical therapy, that has a
    physiological effect on an organism.

    Here the term drug is used interchangeably with the term medicine although clinical
    knowledge make a clear difference between them.
    """
    DrugClass = Schema(schema_storage["DrugClass"])
    """A class of medical drugs, e.g., statins.

    Classes can represent general pharmacological class, common mechanisms of action,
    common physiological effects, etc.
    """
    DrugCost = Schema(schema_storage["DrugCost"])
    """The cost per unit of a medical drug.

    Note that this type is not meant to represent the price in an offer of a drug for
    sale; see the Offer type for that. This type will typically be used to tag wholesale
    or average retail cost of a drug, or maximum reimbursable cost. Costs of medical
    drugs vary widely depending on how and where they are paid for, so while this type
    captures some of the variables, costs should be used with caution by consumers of
    this schema's markup.
    """
    DrugCostCategory = Schema(schema_storage["DrugCostCategory"])
    """Enumerated categories of medical drug costs."""
    DrugLegalStatus = Schema(schema_storage["DrugLegalStatus"])
    """The legal availability status of a medical drug."""
    DrugPregnancyCategory = Schema(schema_storage["DrugPregnancyCategory"])
    """Categories that represent an assessment of the risk of fetal injury due to a drug
    or pharmaceutical used as directed by the mother during pregnancy."""
    DrugPrescriptionStatus = Schema(schema_storage["DrugPrescriptionStatus"])
    """Indicates whether this drug is available by prescription or over-the-counter."""
    DrugStrength = Schema(schema_storage["DrugStrength"])
    """A specific strength in which a medical drug is available in a specific
    country."""
    DryCleaningOrLaundry = Schema(schema_storage["DryCleaningOrLaundry"])
    """A dry-cleaning business."""
    Duration = Schema(schema_storage["Duration"])
    """Quantity: Duration (use <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO 8601 duration format</a>)."""
    EBook = Schema(schema_storage["EBook"])
    """Book format: Ebook."""
    EPRelease = Schema(schema_storage["EPRelease"])
    """EPRelease."""
    EUEnergyEfficiencyCategoryA = Schema(schema_storage["EUEnergyEfficiencyCategoryA"])
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryA1Plus = Schema(
        schema_storage["EUEnergyEfficiencyCategoryA1Plus"]
    )
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryA2Plus = Schema(
        schema_storage["EUEnergyEfficiencyCategoryA2Plus"]
    )
    """Represents EU Energy Efficiency Class A++ as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryA3Plus = Schema(
        schema_storage["EUEnergyEfficiencyCategoryA3Plus"]
    )
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryB = Schema(schema_storage["EUEnergyEfficiencyCategoryB"])
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryC = Schema(schema_storage["EUEnergyEfficiencyCategoryC"])
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryD = Schema(schema_storage["EUEnergyEfficiencyCategoryD"])
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryE = Schema(schema_storage["EUEnergyEfficiencyCategoryE"])
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryF = Schema(schema_storage["EUEnergyEfficiencyCategoryF"])
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyCategoryG = Schema(schema_storage["EUEnergyEfficiencyCategoryG"])
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling
    regulations."""
    EUEnergyEfficiencyEnumeration = Schema(
        schema_storage["EUEnergyEfficiencyEnumeration"]
    )
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as
    defined in EU directive 2017/1369."""
    Ear = Schema(schema_storage["Ear"])
    """Ear function assessment with clinical examination."""
    EatAction = Schema(schema_storage["EatAction"])
    """The act of swallowing solid objects."""
    EditedOrCroppedContent = Schema(schema_storage["EditedOrCroppedContent"])
    """Content coded 'edited or cropped content' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'edited or
    cropped content': The video has been edited or rearranged. This category applies to
    time edits, including editing multiple videos together to alter the story being told
    or editing out large portions from a video.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be 'edited or
    cropped content': Presenting a part of an image from a larger whole to mislead the
    viewer.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'edited or cropped content': Presenting a part of an image from a larger
    whole to mislead the viewer.<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be 'edited or
    cropped content': The audio has been edited or rearranged. This category applies to
    time edits, including editing multiple audio clips together to alter the story being
    told or editing out large portions from the recording.
    """
    EducationEvent = Schema(schema_storage["EducationEvent"])
    """Event type: Education event."""
    EducationalAudience = Schema(schema_storage["EducationalAudience"])
    """An EducationalAudience."""
    EducationalOccupationalCredential = Schema(
        schema_storage["EducationalOccupationalCredential"]
    )
    """An educational or occupational credential.

    A diploma, academic degree, certification, qualification, badge, etc., that may be
    awarded to a person or other entity that meets the requirements defined by the
    credentialer.
    """
    EducationalOccupationalProgram = Schema(
        schema_storage["EducationalOccupationalProgram"]
    )
    """A program offered by an institution which determines the learning progress to
    achieve an outcome, usually a credential like a degree or certificate.

    This would define a discrete set of opportunities (e.g., job, courses) that together
    constitute a program with a clear start, end, set of requirements, and transition to
    a new occupational opportunity (e.g., a job), or sometimes a higher educational
    opportunity (e.g., an advanced degree).
    """
    EducationalOrganization = Schema(schema_storage["EducationalOrganization"])
    """An educational organization."""
    EffectivenessHealthAspect = Schema(schema_storage["EffectivenessHealthAspect"])
    """Content about the effectiveness-related aspects of a health topic."""
    Electrician = Schema(schema_storage["Electrician"])
    """An electrician."""
    ElectronicsStore = Schema(schema_storage["ElectronicsStore"])
    """An electronics store."""
    ElementarySchool = Schema(schema_storage["ElementarySchool"])
    """An elementary school."""
    EmailMessage = Schema(schema_storage["EmailMessage"])
    """An email message."""
    Embassy = Schema(schema_storage["Embassy"])
    """An embassy."""
    Emergency = Schema(schema_storage["Emergency"])
    """A specific branch of medical science that deals with the evaluation and initial
    treatment of medical conditions caused by trauma or sudden illness."""
    EmergencyService = Schema(schema_storage["EmergencyService"])
    """An emergency service, such as a fire station or ER."""
    EmployeeRole = Schema(schema_storage["EmployeeRole"])
    """A subclass of OrganizationRole used to describe employee relationships."""
    EmployerAggregateRating = Schema(schema_storage["EmployerAggregateRating"])
    """An aggregate rating of an Organization related to its role as an employer."""
    EmployerReview = Schema(schema_storage["EmployerReview"])
    """An <a class="localLink" href="#sc.EmployerReview">EmployerReview</a> is a review
    of an <a class="localLink" href="#sc.Organization">Organization</a> regarding its
    role as an employer, written by a current or former employee of that
    organization."""
    EmploymentAgency = Schema(schema_storage["EmploymentAgency"])
    """An employment agency."""
    Endocrine = Schema(schema_storage["Endocrine"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of endocrine glands and their secretions."""
    EndorseAction = Schema(schema_storage["EndorseAction"])
    """An agent approves/certifies/likes/supports/sanction an object."""
    EndorsementRating = Schema(schema_storage["EndorsementRating"])
    """An EndorsementRating is a rating that expresses some level of endorsement, for
    example inclusion in a "critic's pick" blog, a "Like" or "+1" on a social network.
    It can be considered the <a class="localLink" href="#sc.result">result</a> of an <a
    class="localLink" href="#sc.EndorseAction">EndorseAction</a> in which the <a
    class="localLink" href="#sc.object">object</a> of the action is rated positively by
    some <a class="localLink" href="#sc.agent">agent</a>. As is common elsewhere in
    schema.org, it is sometimes more useful to describe the results of such an action
    without explicitly describing the <a class="localLink"
    href="#sc.Action">Action</a>.<br/><br/>

    An <a class="localLink" href="#sc.EndorsementRating">EndorsementRating</a> may be
    part of a numeric scale or organized system, but this is not required: having an
    explicit type for indicating a positive, endorsement rating is particularly useful
    in the absence of numeric scales as it helps consumers understand that the rating is
    broadly positive.
    """
    Energy = Schema(schema_storage["Energy"])
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy
    unit of measure&gt;'."""
    EnergyConsumptionDetails = Schema(schema_storage["EnergyConsumptionDetails"])
    """EnergyConsumptionDetails represents information related to the energy efficiency
    of a product that consumes energy.

    The information that can be provided is based on international regulations such as for example <a href="https://eur-lex.europa.eu/eli/reg/2017/1369/oj">EU directive 2017/1369</a> for energy labeling and the <a href="https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer">Energy labeling rule</a> under the Energy Policy and Conservation Act (EPCA) in the US.
    """
    EnergyEfficiencyEnumeration = Schema(schema_storage["EnergyEfficiencyEnumeration"])
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and
    certifications that are part of several international energy efficiency
    standards."""
    EnergyStarCertified = Schema(schema_storage["EnergyStarCertified"])
    """Represents EnergyStar certification."""
    EnergyStarEnergyEfficiencyEnumeration = Schema(
        schema_storage["EnergyStarEnergyEfficiencyEnumeration"]
    )
    """Used to indicate whether a product is EnergyStar certified."""
    EngineSpecification = Schema(schema_storage["EngineSpecification"])
    """Information about the engine of the vehicle.

    A vehicle can have multiple engines represented by multiple engine specification
    entities.
    """
    EnrollingByInvitation = Schema(schema_storage["EnrollingByInvitation"])
    """Enrolling participants by invitation only."""
    EntertainmentBusiness = Schema(schema_storage["EntertainmentBusiness"])
    """A business providing entertainment."""
    EntryPoint = Schema(schema_storage["EntryPoint"])
    """An entry point, within some Web-based protocol."""
    Enumeration = Schema(schema_storage["Enumeration"])
    """Lists or enumerations—for example, a list of cuisines or music genres, etc."""
    Episode = Schema(schema_storage["Episode"])
    """A media episode (e.g. TV, radio, video game) which can be part of a series or
    season."""
    Event = Schema(schema_storage["Event"])
    """An event happening at a certain time and location, such as a concert, lecture, or
    festival.

    Ticketing information may be added via the <a class="localLink"
    href="#sc.offers">offers</a> property. Repeated events may be structured as separate
    Event objects.
    """
    EventAttendanceModeEnumeration = Schema(
        schema_storage["EventAttendanceModeEnumeration"]
    )
    """An EventAttendanceModeEnumeration value is one of potentially several modes of
    organising an event, relating to whether it is online or offline."""
    EventCancelled = Schema(schema_storage["EventCancelled"])
    """The event has been cancelled.

    If the event has multiple startDate values, all are assumed to be cancelled. Either
    startDate or previousStartDate may be used to specify the event's cancelled date(s).
    """
    EventMovedOnline = Schema(schema_storage["EventMovedOnline"])
    """Indicates that the event was changed to allow online participation.

    See <a class="localLink" href="#sc.eventAttendanceMode">eventAttendanceMode</a> for specifics of whether it is now fully or partially online.
    """
    EventPostponed = Schema(schema_storage["EventPostponed"])
    """The event has been postponed and no new date has been set.

    The event's previousStartDate should be set.
    """
    EventRescheduled = Schema(schema_storage["EventRescheduled"])
    """The event has been rescheduled.

    The event's previousStartDate should be set to the old date and the startDate should
    be set to the event's new date. (If the event has been rescheduled multiple times,
    the previousStartDate property may be repeated).
    """
    EventReservation = Schema(schema_storage["EventReservation"])
    """A reservation for an event like a concert, sporting event, or lecture.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    EventScheduled = Schema(schema_storage["EventScheduled"])
    """The event is taking place or has taken place on the startDate as scheduled.

    Use of this value is optional, as it is assumed by default.
    """
    EventSeries = Schema(schema_storage["EventSeries"])
    """A series of <a class="localLink" href="#sc.Event">Event</a>s. Included events can
    relate with the series using the <a class="localLink"
    href="#sc.superEvent">superEvent</a> property.<br/><br/>

    An EventSeries is a collection of events that share some unifying characteristic.
    For example, "The Olympic Games" is a series, which is repeated regularly. The "2012
    London Olympics" can be presented both as an <a class="localLink"
    href="#sc.Event">Event</a> in the series "Olympic Games", and as an <a
    class="localLink" href="#sc.EventSeries">EventSeries</a> that included a number of
    sporting competitions as Events.<br/><br/>

    The nature of the association between the events in an <a class="localLink"
    href="#sc.EventSeries">EventSeries</a> can vary, but typical examples could include
    a thematic event series (e.g. topical meetups or classes), or a series of regular
    events that share a location, attendee group and/or organizers.<br/><br/>

    EventSeries has been defined as a kind of Event to make it easy for publishers to
    use it in an Event context without worrying about which kinds of series are really
    event-like enough to call an Event. In general an EventSeries may seem more Event-
    like when the period of time is compact and when aspects such as location are fixed,
    but it may also sometimes prove useful to describe a longer-term series as an Event.
    """
    EventStatusType = Schema(schema_storage["EventStatusType"])
    """EventStatusType is an enumeration type whose instances represent several states
    that an Event may be in."""
    EventVenue = Schema(schema_storage["EventVenue"])
    """An event venue."""
    EvidenceLevelA = Schema(schema_storage["EvidenceLevelA"])
    """Data derived from multiple randomized clinical trials or meta-analyses."""
    EvidenceLevelB = Schema(schema_storage["EvidenceLevelB"])
    """Data derived from a single randomized trial, or nonrandomized studies."""
    EvidenceLevelC = Schema(schema_storage["EvidenceLevelC"])
    """Only consensus opinion of experts, case studies, or standard-of-care."""
    ExchangeRateSpecification = Schema(schema_storage["ExchangeRateSpecification"])
    """A structured value representing exchange rate."""
    ExchangeRefund = Schema(schema_storage["ExchangeRefund"])
    """A ExchangeRefund ..."""
    ExerciseAction = Schema(schema_storage["ExerciseAction"])
    """The act of participating in exertive activity for the purposes of improving
    health and fitness."""
    ExerciseGym = Schema(schema_storage["ExerciseGym"])
    """A gym."""
    ExercisePlan = Schema(schema_storage["ExercisePlan"])
    """Fitness-related activity designed for a specific health-related purpose,
    including defined exercise routines as well as activity prescribed by a
    clinician."""
    ExhibitionEvent = Schema(schema_storage["ExhibitionEvent"])
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ..."""
    Eye = Schema(schema_storage["Eye"])
    """Eye or ophtalmological function assessment with clinical examination."""
    FAQPage = Schema(schema_storage["FAQPage"])
    """A <a class="localLink" href="#sc.FAQPage">FAQPage</a> is a <a class="localLink" href="#sc.WebPage">WebPage</a> presenting one or more "<a href="https://en.wikipedia.org/wiki/FAQ">Frequently asked questions</a>" (see also <a class="localLink" href="#sc.QAPage">QAPage</a>)."""
    FDAcategoryA = Schema(schema_storage["FDAcategoryA"])
    """A designation by the US FDA signifying that adequate and well-controlled studies
    have failed to demonstrate a risk to the fetus in the first trimester of pregnancy
    (and there is no evidence of risk in later trimesters)."""
    FDAcategoryB = Schema(schema_storage["FDAcategoryB"])
    """A designation by the US FDA signifying that animal reproduction studies have
    failed to demonstrate a risk to the fetus and there are no adequate and well-
    controlled studies in pregnant women."""
    FDAcategoryC = Schema(schema_storage["FDAcategoryC"])
    """A designation by the US FDA signifying that animal reproduction studies have
    shown an adverse effect on the fetus and there are no adequate and well-controlled
    studies in humans, but potential benefits may warrant use of the drug in pregnant
    women despite potential risks."""
    FDAcategoryD = Schema(schema_storage["FDAcategoryD"])
    """A designation by the US FDA signifying that there is positive evidence of human
    fetal risk based on adverse reaction data from investigational or marketing
    experience or studies in humans, but potential benefits may warrant use of the drug
    in pregnant women despite potential risks."""
    FDAcategoryX = Schema(schema_storage["FDAcategoryX"])
    """A designation by the US FDA signifying that studies in animals or humans have
    demonstrated fetal abnormalities and/or there is positive evidence of human fetal
    risk based on adverse reaction data from investigational or marketing experience,
    and the risks involved in use of the drug in pregnant women clearly outweigh
    potential benefits."""
    FDAnotEvaluated = Schema(schema_storage["FDAnotEvaluated"])
    """A designation that the drug in question has not been assigned a pregnancy
    category designation by the US FDA."""
    FMRadioChannel = Schema(schema_storage["FMRadioChannel"])
    """A radio channel that uses FM."""
    FailedActionStatus = Schema(schema_storage["FailedActionStatus"])
    """An action that failed to complete.

    The action's error property and the HTTP return code contain more information about
    the failure.
    """
    _False = Schema(schema_storage["False"])
    """@public The boolean value false."""
    FastFoodRestaurant = Schema(schema_storage["FastFoodRestaurant"])
    """A fast-food restaurant."""
    Female = Schema(schema_storage["Female"])
    """The female gender."""
    Festival = Schema(schema_storage["Festival"])
    """Event type: Festival."""
    FilmAction = Schema(schema_storage["FilmAction"])
    """The act of capturing sound and moving images on film, video, or digitally."""
    FinancialProduct = Schema(schema_storage["FinancialProduct"])
    """A product provided to consumers and businesses by financial institutions such as
    banks, insurance companies, brokerage firms, consumer finance companies, and
    investment companies which comprise the financial services industry."""
    FinancialService = Schema(schema_storage["FinancialService"])
    """Financial services business."""
    FindAction = Schema(schema_storage["FindAction"])
    """The act of finding an object.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.SearchAction">SearchAction</a>: FindAction
    is generally lead by a SearchAction, but not necessarily.</li> </ul>
    """
    FireStation = Schema(schema_storage["FireStation"])
    """A fire station.

    With firemen.
    """
    Flexibility = Schema(schema_storage["Flexibility"])
    """Physical activity that is engaged in to improve joint and muscle flexibility."""
    Flight = Schema(schema_storage["Flight"])
    """An airline flight."""
    FlightReservation = Schema(schema_storage["FlightReservation"])
    """A reservation for air travel.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    Float = Schema(schema_storage["Float"])
    """Data type: Floating number."""
    FloorPlan = Schema(schema_storage["FloorPlan"])
    """A FloorPlan is an explicit representation of a collection of similar
    accommodations, allowing the provision of common information (room counts, sizes,
    layout diagrams) and offers for rental or sale.

    In typical use, some <a class="localLink" href="#sc.ApartmentComplex">ApartmentComplex</a> has an <a class="localLink" href="#sc.accommodationFloorPlan">accommodationFloorPlan</a> which is a <a class="localLink" href="#sc.FloorPlan">FloorPlan</a>.  A FloorPlan is always in the context of a particular place, either a larger <a class="localLink" href="#sc.ApartmentComplex">ApartmentComplex</a> or a single <a class="localLink" href="#sc.Apartment">Apartment</a>. The visual/spatial aspects of a floor plan (i.e. room layout, <a href="https://en.wikipedia.org/wiki/Floor_plan">see wikipedia</a>) can be indicated using <a class="localLink" href="#sc.image">image</a>.
    """
    Florist = Schema(schema_storage["Florist"])
    """A florist."""
    FollowAction = Schema(schema_storage["FollowAction"])
    """The act of forming a personal connection with someone/something (object)
    unidirectionally/asymmetrically to get updates polled from.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.BefriendAction">BefriendAction</a>: Unlike
    BefriendAction, FollowAction implies that the connection is <em>not</em> necessarily
    reciprocal.</li> <li><a class="localLink"
    href="#sc.SubscribeAction">SubscribeAction</a>: Unlike SubscribeAction, FollowAction
    implies that the follower acts as an active agent constantly/actively polling for
    updates.</li> <li><a class="localLink" href="#sc.RegisterAction">RegisterAction</a>:
    Unlike RegisterAction, FollowAction implies that the agent is interested in
    continuing receiving updates from the object.</li> <li><a class="localLink"
    href="#sc.JoinAction">JoinAction</a>: Unlike JoinAction, FollowAction implies that
    the agent is interested in getting updates from the object.</li> <li><a
    class="localLink" href="#sc.TrackAction">TrackAction</a>: Unlike TrackAction,
    FollowAction refers to the polling of updates of all aspects of animate objects
    rather than the location of inanimate objects (e.g. you track a package, but you
    don't follow it).</li> </ul>
    """
    FoodEstablishment = Schema(schema_storage["FoodEstablishment"])
    """A food-related business."""
    FoodEstablishmentReservation = Schema(
        schema_storage["FoodEstablishmentReservation"]
    )
    """A reservation to dine at a food-related business.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    FoodEvent = Schema(schema_storage["FoodEvent"])
    """Event type: Food event."""
    FoodService = Schema(schema_storage["FoodService"])
    """A food service, like breakfast, lunch, or dinner."""
    FourWheelDriveConfiguration = Schema(schema_storage["FourWheelDriveConfiguration"])
    """Four-wheel drive is a transmission layout where the engine primarily drives two
    wheels with a part-time four-wheel drive capability."""
    Friday = Schema(schema_storage["Friday"])
    """The day of the week between Thursday and Saturday."""
    FrontWheelDriveConfiguration = Schema(
        schema_storage["FrontWheelDriveConfiguration"]
    )
    """Front-wheel drive is a transmission layout where the engine drives the front
    wheels."""
    FullRefund = Schema(schema_storage["FullRefund"])
    """A FullRefund ..."""
    FundingAgency = Schema(schema_storage["FundingAgency"])
    """A FundingAgency is an organization that implements one or more <a
    class="localLink" href="#sc.FundingScheme">FundingScheme</a>s and manages the
    granting process (via <a class="localLink" href="#sc.Grant">Grant</a>s, typically <a
    class="localLink" href="#sc.MonetaryGrant">MonetaryGrant</a>s). A funding agency is
    not always required for grant funding, e.g. philanthropic giving, corporate
    sponsorship etc.<br/><br/>

    Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation...
    """
    FundingScheme = Schema(schema_storage["FundingScheme"])
    """A FundingScheme combines organizational, project and policy aspects of grant-
    based funding.

    that sets guidelines, principles and mechanisms to support other kinds of projects and activities.
    Funding is typically organized via <a class="localLink" href="#sc.Grant">Grant</a> funding. Examples of funding schemes: Swiss Priority Programmes (SPPs); EU Framework 7 (FP7); Horizon 2020; the NIH-R01 Grant Program; Wellcome institutional strategic support fund. For large scale public sector funding, the management and administration of grant awards is often handled by other, dedicated, organizations - <a class="localLink" href="#sc.FundingAgency">FundingAgency</a>s such as ERC, REA, ...
    """
    Fungus = Schema(schema_storage["Fungus"])
    """Pathogenic fungus."""
    FurnitureStore = Schema(schema_storage["FurnitureStore"])
    """A furniture store."""
    Game = Schema(schema_storage["Game"])
    """The Game type represents things which are games.

    These are typically rule-governed recreational activities, e.g. role-playing games
    in which players assume the role of characters in a fictional setting.
    """
    GamePlayMode = Schema(schema_storage["GamePlayMode"])
    """Indicates whether this game is multi-player, co-op or single-player."""
    GameServer = Schema(schema_storage["GameServer"])
    """Server that provides game interaction in a multiplayer game."""
    GameServerStatus = Schema(schema_storage["GameServerStatus"])
    """Status of a game server."""
    GardenStore = Schema(schema_storage["GardenStore"])
    """A garden store."""
    GasStation = Schema(schema_storage["GasStation"])
    """A gas station."""
    Gastroenterologic = Schema(schema_storage["Gastroenterologic"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of digestive system."""
    GatedResidenceCommunity = Schema(schema_storage["GatedResidenceCommunity"])
    """Residence type: Gated community."""
    GenderType = Schema(schema_storage["GenderType"])
    """An enumeration of genders."""
    GeneralContractor = Schema(schema_storage["GeneralContractor"])
    """A general contractor."""
    Genetic = Schema(schema_storage["Genetic"])
    """A specific branch of medical science that pertains to hereditary transmission and
    the variation of inherited characteristics and disorders."""
    Genitourinary = Schema(schema_storage["Genitourinary"])
    """Genitourinary system function assessment with clinical examination."""
    GeoCircle = Schema(schema_storage["GeoCircle"])
    """A GeoCircle is a GeoShape representing a circular geographic area.

    As it is a GeoShape it provides the simple textual property 'circle', but also
    allows the combination of postalCode alongside geoRadius. The center of the circle
    can be indicated via the 'geoMidpoint' property, or more approximately using
    'address', 'postalCode'.
    """
    GeoCoordinates = Schema(schema_storage["GeoCoordinates"])
    """The geographic coordinates of a place or event."""
    GeoShape = Schema(schema_storage["GeoShape"])
    """The geographic shape of a place.

    A GeoShape can be described using several properties whose values are based on
    latitude/longitude pairs. Either whitespace or commas can be used to separate
    latitude and longitude; whitespace should be used when writing a list of several
    such points.
    """
    GeospatialGeometry = Schema(schema_storage["GeospatialGeometry"])
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate
    definitions from Geo-Spatial best practices."""
    Geriatric = Schema(schema_storage["Geriatric"])
    """A specific branch of medical science that is concerned with the diagnosis and
    treatment of diseases, debilities and provision of care to the aged."""
    GettingAccessHealthAspect = Schema(schema_storage["GettingAccessHealthAspect"])
    """Content that discusses practical and policy aspects for getting access to
    specific kinds of healthcare (e.g. distribution mechanisms for vaccines)."""
    GiveAction = Schema(schema_storage["GiveAction"])
    """The act of transferring ownership of an object to a destination. Reciprocal of
    TakeAction.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.TakeAction">TakeAction</a>: Reciprocal of
    GiveAction.</li> <li><a class="localLink" href="#sc.SendAction">SendAction</a>:
    Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I
    may send my laptop to you, but that doesn't mean I'm giving it to you).</li> </ul>
    """
    GlutenFreeDiet = Schema(schema_storage["GlutenFreeDiet"])
    """A diet exclusive of gluten."""
    GolfCourse = Schema(schema_storage["GolfCourse"])
    """A golf course."""
    GovernmentBenefitsType = Schema(schema_storage["GovernmentBenefitsType"])
    """GovernmentBenefitsType enumerates several kinds of government benefits to support
    the COVID-19 situation.

    Note that this structure may not capture all benefits offered.
    """
    GovernmentBuilding = Schema(schema_storage["GovernmentBuilding"])
    """A government building."""
    GovernmentOffice = Schema(schema_storage["GovernmentOffice"])
    """A government office&#x2014;for example, an IRS or DMV office."""
    GovernmentOrganization = Schema(schema_storage["GovernmentOrganization"])
    """A governmental organization or agency."""
    GovernmentPermit = Schema(schema_storage["GovernmentPermit"])
    """A permit issued by a government agency."""
    GovernmentService = Schema(schema_storage["GovernmentService"])
    """A service provided by a government organization, e.g. food stamps, veterans
    benefits, etc."""
    Grant = Schema(schema_storage["Grant"])
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a
    <a class="localLink" href="#sc.funder">funder</a> sponsors some <a class="localLink"
    href="#sc.MonetaryAmount">MonetaryAmount</a> to an <a class="localLink"
    href="#sc.Organization">Organization</a> or <a class="localLink"
    href="#sc.Person">Person</a>, sometimes not necessarily via a dedicated or long-
    lived <a class="localLink" href="#sc.Project">Project</a>, resulting in one or more
    outputs, or <a class="localLink" href="#sc.fundedItem">fundedItem</a>s. For
    financial sponsorship, indicate the <a class="localLink"
    href="#sc.funder">funder</a> of a <a class="localLink"
    href="#sc.MonetaryGrant">MonetaryGrant</a>. For non-financial support, indicate <a
    class="localLink" href="#sc.sponsor">sponsor</a> of <a class="localLink"
    href="#sc.Grant">Grant</a>s of resources (e.g. office space).<br/><br/>

    Grants support  activities directed towards some agreed collective goals, often but
    not always organized as <a class="localLink" href="#sc.Project">Project</a>s. Long-
    lived projects are sometimes sponsored by a variety of grants over time, but it is
    also common for a project to be associated with a single grant.<br/><br/>

    The amount of a <a class="localLink" href="#sc.Grant">Grant</a> is represented using
    <a class="localLink" href="#sc.amount">amount</a> as a <a class="localLink"
    href="#sc.MonetaryAmount">MonetaryAmount</a>.
    """
    GraphicNovel = Schema(schema_storage["GraphicNovel"])
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances."""
    GroceryStore = Schema(schema_storage["GroceryStore"])
    """A grocery store."""
    GroupBoardingPolicy = Schema(schema_storage["GroupBoardingPolicy"])
    """The airline boards by groups based on check-in time, priority, etc."""
    Guide = Schema(schema_storage["Guide"])
    """<a class="localLink" href="#sc.Guide">Guide</a> is a page or article that
    recommend specific products or services, or aspects of a thing for a user to
    consider.

    A <a class="localLink" href="#sc.Guide">Guide</a> may represent a Buying Guide and
    detail aspects of products or services for a user to consider. A <a
    class="localLink" href="#sc.Guide">Guide</a> may represent a Product Guide and
    recommend specific products or services. A <a class="localLink"
    href="#sc.Guide">Guide</a> may represent a Ranked List and recommend specific
    products or services with ranking.
    """
    Gynecologic = Schema(schema_storage["Gynecologic"])
    """A specific branch of medical science that pertains to the health care of women,
    particularly in the diagnosis and treatment of disorders affecting the female
    reproductive system."""
    HVACBusiness = Schema(schema_storage["HVACBusiness"])
    """A business that provide Heating, Ventilation and Air Conditioning services."""
    Hackathon = Schema(schema_storage["Hackathon"])
    """A <a href="https://en.wikipedia.org/wiki/Hackathon">hackathon</a> event."""
    HairSalon = Schema(schema_storage["HairSalon"])
    """A hair salon."""
    HalalDiet = Schema(schema_storage["HalalDiet"])
    """A diet conforming to Islamic dietary practices."""
    Hardcover = Schema(schema_storage["Hardcover"])
    """Book format: Hardcover."""
    HardwareStore = Schema(schema_storage["HardwareStore"])
    """A hardware store."""
    Head = Schema(schema_storage["Head"])
    """Head assessment with clinical examination."""
    HealthAndBeautyBusiness = Schema(schema_storage["HealthAndBeautyBusiness"])
    """Health and beauty."""
    HealthAspectEnumeration = Schema(schema_storage["HealthAspectEnumeration"])
    """HealthAspectEnumeration enumerates several aspects of health content online, each
    of which might be described using <a class="localLink"
    href="#sc.hasHealthAspect">hasHealthAspect</a> and <a class="localLink"
    href="#sc.HealthTopicContent">HealthTopicContent</a>."""
    HealthCare = Schema(schema_storage["HealthCare"])
    """HealthCare: this is a benefit for health care."""
    HealthClub = Schema(schema_storage["HealthClub"])
    """A health club."""
    HealthInsurancePlan = Schema(schema_storage["HealthInsurancePlan"])
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs."""
    HealthPlanCostSharingSpecification = Schema(
        schema_storage["HealthPlanCostSharingSpecification"]
    )
    """A description of costs to the patient under a given network or formulary."""
    HealthPlanFormulary = Schema(schema_storage["HealthPlanFormulary"])
    """For a given health insurance plan, the specification for costs and coverage of
    prescription drugs."""
    HealthPlanNetwork = Schema(schema_storage["HealthPlanNetwork"])
    """A US-style health insurance plan network."""
    HealthTopicContent = Schema(schema_storage["HealthTopicContent"])
    """<a class="localLink" href="#sc.HealthTopicContent">HealthTopicContent</a> is <a
    class="localLink" href="#sc.WebContent">WebContent</a> that is about some aspect of
    a health topic, e.g. a condition, its symptoms or treatments.

    Such content may be comprised of several parts or sections and use different types of media. Multiple instances of <a class="localLink" href="#sc.WebContent">WebContent</a> (and hence <a class="localLink" href="#sc.HealthTopicContent">HealthTopicContent</a>) can be related using <a class="localLink" href="#sc.hasPart">hasPart</a> / <a class="localLink" href="#sc.isPartOf">isPartOf</a> where there is some kind of content hierarchy, and their content described with <a class="localLink" href="#sc.about">about</a> and <a class="localLink" href="#sc.mentions">mentions</a> e.g. building upon the existing <a class="localLink" href="#sc.MedicalCondition">MedicalCondition</a> vocabulary.
    """
    HearingImpairedSupported = Schema(schema_storage["HearingImpairedSupported"])
    """Uses devices to support users with hearing impairments."""
    Hematologic = Schema(schema_storage["Hematologic"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of blood and blood producing organs."""
    HighSchool = Schema(schema_storage["HighSchool"])
    """A high school."""
    HinduDiet = Schema(schema_storage["HinduDiet"])
    """A diet conforming to Hindu dietary practices, in particular, beef-free."""
    HinduTemple = Schema(schema_storage["HinduTemple"])
    """A Hindu temple."""
    HobbyShop = Schema(schema_storage["HobbyShop"])
    """A store that sells materials useful or necessary for various hobbies."""
    HomeAndConstructionBusiness = Schema(schema_storage["HomeAndConstructionBusiness"])
    """A construction business.<br/><br/>

    A HomeAndConstructionBusiness is a <a class="localLink"
    href="#sc.LocalBusiness">LocalBusiness</a> that provides services around homes and
    buildings.<br/><br/>

    As a <a class="localLink" href="#sc.LocalBusiness">LocalBusiness</a> it can be
    described as a <a class="localLink" href="#sc.provider">provider</a> of one or more
    <a class="localLink" href="#sc.Service">Service</a>(s).
    """
    HomeGoodsStore = Schema(schema_storage["HomeGoodsStore"])
    """A home goods store."""
    Homeopathic = Schema(schema_storage["Homeopathic"])
    """A system of medicine based on the principle that a disease can be cured by a
    substance that produces similar symptoms in healthy people."""
    Hospital = Schema(schema_storage["Hospital"])
    """A hospital."""
    Hostel = Schema(schema_storage["Hostel"])
    """A hostel - cheap accommodation, often in shared dormitories.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    Hotel = Schema(schema_storage["Hotel"])
    """A hotel is an establishment that provides lodging paid on a short-term basis (Source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    HotelRoom = Schema(schema_storage["HotelRoom"])
    """A hotel room is a single room in a hotel.

    <br /><br /> See also the <a href="/docs/hotels.html">dedicated document on the use
    of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    House = Schema(schema_storage["House"])
    """A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/House">http://en.wikipedia.org/wiki/House</a>)."""
    HousePainter = Schema(schema_storage["HousePainter"])
    """A house painting service."""
    HowItWorksHealthAspect = Schema(schema_storage["HowItWorksHealthAspect"])
    """Content that discusses and explains how a particular health-related topic works,
    e.g. in terms of mechanisms and underlying science."""
    HowOrWhereHealthAspect = Schema(schema_storage["HowOrWhereHealthAspect"])
    """Information about how or where to find a topic.

    Also may contain location data that can be used for where to look for help if the
    topic is observed.
    """
    HowTo = Schema(schema_storage["HowTo"])
    """Instructions that explain how to achieve a result by performing a sequence of
    steps."""
    HowToDirection = Schema(schema_storage["HowToDirection"])
    """A direction indicating a single action to do in the instructions for how to
    achieve a result."""
    HowToItem = Schema(schema_storage["HowToItem"])
    """An item used as either a tool or supply when performing the instructions for how
    to to achieve a result."""
    HowToSection = Schema(schema_storage["HowToSection"])
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g.
    steps for making a pie crust within a pie recipe)."""
    HowToStep = Schema(schema_storage["HowToStep"])
    """A step in the instructions for how to achieve a result.

    It is an ordered list with HowToDirection and/or HowToTip items.
    """
    HowToSupply = Schema(schema_storage["HowToSupply"])
    """A supply consumed when performing the instructions for how to achieve a
    result."""
    HowToTip = Schema(schema_storage["HowToTip"])
    """An explanation in the instructions for how to achieve a result.

    It provides supplementary information about a technique, supply, author's
    preference, etc. It can explain what could be done, or what should not be done, but
    doesn't specify what should be done (see HowToDirection).
    """
    HowToTool = Schema(schema_storage["HowToTool"])
    """A tool used (but not consumed) when performing instructions for how to achieve a
    result."""
    HyperToc = Schema(schema_storage["HyperToc"])
    """A HyperToc represents a hypertext table of contents for complex media objects,
    such as <a class="localLink" href="#sc.VideoObject">VideoObject</a>, <a
    class="localLink" href="#sc.AudioObject">AudioObject</a>.

    Items in the table of contents are indicated using the <a class="localLink"
    href="#sc.tocEntry">tocEntry</a> property, and typed <a class="localLink"
    href="#sc.HyperTocEntry">HyperTocEntry</a>. For cases where the same larger work is
    split into multiple files, <a class="localLink"
    href="#sc.associatedMedia">associatedMedia</a> can be used on individual <a
    class="localLink" href="#sc.HyperTocEntry">HyperTocEntry</a> items.
    """
    HyperTocEntry = Schema(schema_storage["HyperTocEntry"])
    """A HyperToEntry is an item within a <a class="localLink"
    href="#sc.HyperToc">HyperToc</a>, which represents a hypertext table of contents for
    complex media objects, such as <a class="localLink"
    href="#sc.VideoObject">VideoObject</a>, <a class="localLink"
    href="#sc.AudioObject">AudioObject</a>.

    The media object itself is indicated using <a class="localLink"
    href="#sc.associatedMedia">associatedMedia</a>. Each section of interest within that
    content can be described with a <a class="localLink"
    href="#sc.HyperTocEntry">HyperTocEntry</a>, with associated <a class="localLink"
    href="#sc.startOffset">startOffset</a> and <a class="localLink"
    href="#sc.endOffset">endOffset</a>. When several entries are all from the same file,
    <a class="localLink" href="#sc.associatedMedia">associatedMedia</a> is used on the
    overarching <a class="localLink" href="#sc.HyperTocEntry">HyperTocEntry</a>; if the
    content has been split into multiple files, they can be referenced using <a
    class="localLink" href="#sc.associatedMedia">associatedMedia</a> on each <a
    class="localLink" href="#sc.HyperTocEntry">HyperTocEntry</a>.
    """
    IceCreamShop = Schema(schema_storage["IceCreamShop"])
    """An ice cream shop."""
    IgnoreAction = Schema(schema_storage["IgnoreAction"])
    """The act of intentionally disregarding the object.

    An agent ignores an object.
    """
    ImageGallery = Schema(schema_storage["ImageGallery"])
    """Web page type: Image gallery page."""
    ImageObject = Schema(schema_storage["ImageObject"])
    """An image file."""
    ImagingTest = Schema(schema_storage["ImagingTest"])
    """Any medical imaging modality typically used for diagnostic purposes."""
    InForce = Schema(schema_storage["InForce"])
    """Indicates that a legislation is in force."""
    InStock = Schema(schema_storage["InStock"])
    """Indicates that the item is in stock."""
    InStoreOnly = Schema(schema_storage["InStoreOnly"])
    """Indicates that the item is available only at physical locations."""
    IndividualProduct = Schema(schema_storage["IndividualProduct"])
    """A single, identifiable product instance (e.g. a laptop with a particular serial
    number)."""
    Infectious = Schema(schema_storage["Infectious"])
    """Something in medical science that pertains to infectious diseases i.e caused by
    bacterial, viral, fungal or parasitic infections."""
    InfectiousAgentClass = Schema(schema_storage["InfectiousAgentClass"])
    """Classes of agents or pathogens that transmit infectious diseases.

    Enumerated type.
    """
    InfectiousDisease = Schema(schema_storage["InfectiousDisease"])
    """An infectious disease is a clinically evident human disease resulting from the
    presence of pathogenic microbial agents, like pathogenic viruses, pathogenic
    bacteria, fungi, protozoa, multicellular parasites, and prions.

    To be considered an infectious disease, such pathogens are known to be able to cause
    this disease.
    """
    InformAction = Schema(schema_storage["InformAction"])
    """The act of notifying someone of information pertinent to them, with no
    expectation of a response."""
    IngredientsHealthAspect = Schema(schema_storage["IngredientsHealthAspect"])
    """Content discussing ingredients-related aspects of a health topic."""
    InsertAction = Schema(schema_storage["InsertAction"])
    """The act of adding at a specific location in an ordered collection."""
    InstallAction = Schema(schema_storage["InstallAction"])
    """The act of installing an application."""
    Installment = Schema(schema_storage["Installment"])
    """Represents the installment pricing component of the total price for an offered
    product."""
    InsuranceAgency = Schema(schema_storage["InsuranceAgency"])
    """An Insurance agency."""
    Intangible = Schema(schema_storage["Intangible"])
    """A utility class that serves as the umbrella for a number of 'intangible' things
    such as quantities, structured values, etc."""
    Integer = Schema(schema_storage["Integer"])
    """Data type: Integer."""
    InteractAction = Schema(schema_storage["InteractAction"])
    """The act of interacting with another person or organization."""
    InteractionCounter = Schema(schema_storage["InteractionCounter"])
    """A summary of how users have interacted with this CreativeWork.

    In most cases, authors will use a subtype to specify the specific type of
    interaction.
    """
    InternationalTrial = Schema(schema_storage["InternationalTrial"])
    """An international trial."""
    InternetCafe = Schema(schema_storage["InternetCafe"])
    """An internet cafe."""
    InvestmentFund = Schema(schema_storage["InvestmentFund"])
    """A company or fund that gathers capital from a number of investors to create a
    pool of money that is then re-invested into stocks, bonds and other assets."""
    InvestmentOrDeposit = Schema(schema_storage["InvestmentOrDeposit"])
    """A type of financial product that typically requires the client to transfer funds
    to a financial service in return for potential beneficial financial return."""
    InviteAction = Schema(schema_storage["InviteAction"])
    """The act of asking someone to attend an event.

    Reciprocal of RsvpAction.
    """
    Invoice = Schema(schema_storage["Invoice"])
    """A statement of the money due for goods or services; a bill."""
    InvoicePrice = Schema(schema_storage["InvoicePrice"])
    """Represents the invoice price of an offered product."""
    ItemAvailability = Schema(schema_storage["ItemAvailability"])
    """A list of possible product availability options."""
    ItemList = Schema(schema_storage["ItemList"])
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen,
    or Top 100 Party Songs.

    Not to be confused with HTML lists, which are often used only for formatting.
    """
    ItemListOrderAscending = Schema(schema_storage["ItemListOrderAscending"])
    """An ItemList ordered with lower values listed first."""
    ItemListOrderDescending = Schema(schema_storage["ItemListOrderDescending"])
    """An ItemList ordered with higher values listed first."""
    ItemListOrderType = Schema(schema_storage["ItemListOrderType"])
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is
    organized."""
    ItemListUnordered = Schema(schema_storage["ItemListUnordered"])
    """An ItemList ordered with no explicit order."""
    ItemPage = Schema(schema_storage["ItemPage"])
    """A page devoted to a single item, such as a particular product or hotel."""
    JewelryStore = Schema(schema_storage["JewelryStore"])
    """A jewelry store."""
    JobPosting = Schema(schema_storage["JobPosting"])
    """A listing that describes a job opening in a certain organization."""
    JoinAction = Schema(schema_storage["JoinAction"])
    """An agent joins an event/group with participants/friends at a location.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.RegisterAction">RegisterAction</a>: Unlike
    RegisterAction, JoinAction refers to joining a group/team of people.</li> <li><a
    class="localLink" href="#sc.SubscribeAction">SubscribeAction</a>: Unlike
    SubscribeAction, JoinAction does not imply that you'll be receiving updates.</li>
    <li><a class="localLink" href="#sc.FollowAction">FollowAction</a>: Unlike
    FollowAction, JoinAction does not imply that you'll be polling for updates.</li>
    </ul>
    """
    Joint = Schema(schema_storage["Joint"])
    """The anatomical location at which two or more bones make contact."""
    KosherDiet = Schema(schema_storage["KosherDiet"])
    """A diet conforming to Jewish dietary practices."""
    LaboratoryScience = Schema(schema_storage["LaboratoryScience"])
    """A medical science pertaining to chemical, hematological, immunologic,
    microscopic, or bacteriological diagnostic analyses or research."""
    LakeBodyOfWater = Schema(schema_storage["LakeBodyOfWater"])
    """A lake (for example, Lake Pontrachain)."""
    Landform = Schema(schema_storage["Landform"])
    """A landform or physical feature.

    Landform elements include mountains, plains, lakes, rivers, seascape and oceanic
    waterbody interface features such as bays, peninsulas, seas and so forth, including
    sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the
    great ocean basins.
    """
    LandmarksOrHistoricalBuildings = Schema(
        schema_storage["LandmarksOrHistoricalBuildings"]
    )
    """An historical landmark or building."""
    Language = Schema(schema_storage["Language"])
    """Natural languages such as Spanish, Tamil, Hindi, English, etc.

    Formal language code tags expressed in <a href="https://en.wikipedia.org/wiki/IETF_language_tag">BCP 47</a> can be used via the <a class="localLink" href="#sc.alternateName">alternateName</a> property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using <a class="localLink" href="#sc.ComputerLanguage">ComputerLanguage</a>.
    """
    LaserDiscFormat = Schema(schema_storage["LaserDiscFormat"])
    """LaserDiscFormat."""
    LearningResource = Schema(schema_storage["LearningResource"])
    """The LearningResource type can be used to indicate <a class="localLink"
    href="#sc.CreativeWork">CreativeWork</a>s (whether physical or digital) that have a
    particular and explicit orientation towards learning, education, skill acquisition,
    and other educational purposes.<br/><br/>

    <a class="localLink" href="#sc.LearningResource">LearningResource</a> is expected to
    be used as an addition to a primary type such as <a class="localLink"
    href="#sc.Book">Book</a>, <a class="localLink"
    href="#sc.VideoObject">VideoObject</a>, <a class="localLink"
    href="#sc.Product">Product</a> etc.<br/><br/>

    <a class="localLink" href="#sc.EducationEvent">EducationEvent</a> serves a similar
    purpose for event-like things (e.g. a <a class="localLink"
    href="#sc.Trip">Trip</a>). A <a class="localLink"
    href="#sc.LearningResource">LearningResource</a> may be created as a result of an <a
    class="localLink" href="#sc.EducationEvent">EducationEvent</a>, for example by
    recording one.
    """
    LeaveAction = Schema(schema_storage["LeaveAction"])
    """An agent leaves an event / group with participants/friends at a
    location.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.JoinAction">JoinAction</a>: The antonym of
    LeaveAction.</li> <li><a class="localLink"
    href="#sc.UnRegisterAction">UnRegisterAction</a>: Unlike UnRegisterAction,
    LeaveAction implies leaving a group/team of people rather than a service.</li> </ul>
    """
    LeftHandDriving = Schema(schema_storage["LeftHandDriving"])
    """The steering position is on the left side of the vehicle (viewed from the main
    direction of driving)."""
    LegalForceStatus = Schema(schema_storage["LegalForceStatus"])
    """A list of possible statuses for the legal force of a legislation."""
    LegalService = Schema(schema_storage["LegalService"])
    """A LegalService is a business that provides legally-oriented services, advice and
    representation, e.g. law firms.<br/><br/>

    As a <a class="localLink" href="#sc.LocalBusiness">LocalBusiness</a> it can be
    described as a <a class="localLink" href="#sc.provider">provider</a> of one or more
    <a class="localLink" href="#sc.Service">Service</a>(s).
    """
    LegalValueLevel = Schema(schema_storage["LegalValueLevel"])
    """A list of possible levels for the legal validity of a legislation."""
    Legislation = Schema(schema_storage["Legislation"])
    """A legal document such as an act, decree, bill, etc.

    (enforceable or not) or a component of a legal act (like an article).
    """
    LegislationObject = Schema(schema_storage["LegislationObject"])
    """A specific object or file containing a Legislation.

    Note that the same Legislation can be published in multiple files. For example, a
    digitally signed PDF, a plain PDF and an HTML version.
    """
    LegislativeBuilding = Schema(schema_storage["LegislativeBuilding"])
    """A legislative building&#x2014;for example, the state capitol."""
    LeisureTimeActivity = Schema(schema_storage["LeisureTimeActivity"])
    """Any physical activity engaged in for recreational purposes.

    Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.
    """
    LendAction = Schema(schema_storage["LendAction"])
    """The act of providing an object under an agreement that it will be returned at a
    later date. Reciprocal of BorrowAction.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.BorrowAction">BorrowAction</a>: Reciprocal
    of LendAction.</li> </ul>
    """
    Library = Schema(schema_storage["Library"])
    """A library."""
    LibrarySystem = Schema(schema_storage["LibrarySystem"])
    """A <a class="localLink" href="#sc.LibrarySystem">LibrarySystem</a> is a
    collaborative system amongst several libraries."""
    LifestyleModification = Schema(schema_storage["LifestyleModification"])
    """A process of care involving exercise, changes to diet, fitness routines, and
    other lifestyle changes aimed at improving a health condition."""
    Ligament = Schema(schema_storage["Ligament"])
    """A short band of tough, flexible, fibrous connective tissue that functions to
    connect multiple bones, cartilages, and structurally support joints."""
    LikeAction = Schema(schema_storage["LikeAction"])
    """The act of expressing a positive sentiment about the object.

    An agent likes an object (a proposition, topic or theme) with participants.
    """
    LimitedAvailability = Schema(schema_storage["LimitedAvailability"])
    """Indicates that the item has limited availability."""
    LimitedByGuaranteeCharity = Schema(schema_storage["LimitedByGuaranteeCharity"])
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK)."""
    LinkRole = Schema(schema_storage["LinkRole"])
    """A Role that represents a Web link e.g. as expressed via the 'url' property.

    Its linkRelationship property can indicate URL-based and plain textual link types
    e.g. those in IANA link registry or others such as 'amphtml'. This structure
    provides a placeholder where details from HTML's link element can be represented
    outside of HTML, e.g. in JSON-LD feeds.
    """
    LiquorStore = Schema(schema_storage["LiquorStore"])
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other
    spirits."""
    ListItem = Schema(schema_storage["ListItem"])
    """An list item, e.g. a step in a checklist or how-to description."""
    ListPrice = Schema(schema_storage["ListPrice"])
    """Represents the list price (the price a product is actually advertised for) of an
    offered product."""
    ListenAction = Schema(schema_storage["ListenAction"])
    """The act of consuming audio content."""
    LiteraryEvent = Schema(schema_storage["LiteraryEvent"])
    """Event type: Literary event."""
    LiveAlbum = Schema(schema_storage["LiveAlbum"])
    """LiveAlbum."""
    LiveBlogPosting = Schema(schema_storage["LiveBlogPosting"])
    """A blog post intended to provide a rolling textual coverage of an ongoing event
    through continuous updates."""
    LivingWithHealthAspect = Schema(schema_storage["LivingWithHealthAspect"])
    """Information about coping or life related to the topic."""
    LoanOrCredit = Schema(schema_storage["LoanOrCredit"])
    """A financial product for the loaning of an amount of money, or line of credit,
    under agreed terms and charges."""
    LocalBusiness = Schema(schema_storage["LocalBusiness"])
    """A particular physical business or branch of an organization.

    Examples of LocalBusiness include a restaurant, a particular branch of a restaurant
    chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.
    """
    LocationFeatureSpecification = Schema(
        schema_storage["LocationFeatureSpecification"]
    )
    """Specifies a location feature by providing a structured value representing a
    feature of an accommodation as a property-value pair of varying degrees of
    formality."""
    LockerDelivery = Schema(schema_storage["LockerDelivery"])
    """A DeliveryMethod in which an item is made available via locker."""
    Locksmith = Schema(schema_storage["Locksmith"])
    """A locksmith."""
    LodgingBusiness = Schema(schema_storage["LodgingBusiness"])
    """A lodging business, such as a motel, hotel, or inn."""
    LodgingReservation = Schema(schema_storage["LodgingReservation"])
    """A reservation for lodging at a hotel, motel, inn, etc.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    Longitudinal = Schema(schema_storage["Longitudinal"])
    """Unlike cross-sectional studies, longitudinal studies track the same people, and
    therefore the differences observed in those people are less likely to be the result
    of cultural differences across generations.

    Longitudinal studies are also used in medicine to uncover predictors of certain
    diseases.
    """
    LoseAction = Schema(schema_storage["LoseAction"])
    """The act of being defeated in a competitive activity."""
    LowCalorieDiet = Schema(schema_storage["LowCalorieDiet"])
    """A diet focused on reduced calorie intake."""
    LowFatDiet = Schema(schema_storage["LowFatDiet"])
    """A diet focused on reduced fat and cholesterol intake."""
    LowLactoseDiet = Schema(schema_storage["LowLactoseDiet"])
    """A diet appropriate for people with lactose intolerance."""
    LowSaltDiet = Schema(schema_storage["LowSaltDiet"])
    """A diet focused on reduced sodium intake."""
    Lung = Schema(schema_storage["Lung"])
    """Lung and respiratory system clinical examination."""
    LymphaticVessel = Schema(schema_storage["LymphaticVessel"])
    """A type of blood vessel that specifically carries lymph fluid unidirectionally
    toward the heart."""
    MRI = Schema(schema_storage["MRI"])
    """Magnetic resonance imaging."""
    MSRP = Schema(schema_storage["MSRP"])
    """Represents the manufacturer suggested retail price ("MSRP") of an offered
    product."""
    Male = Schema(schema_storage["Male"])
    """The male gender."""
    Manuscript = Schema(schema_storage["Manuscript"])
    """A book, document, or piece of music written by hand rather than typed or
    printed."""
    Map = Schema(schema_storage["Map"])
    """A map."""
    MapCategoryType = Schema(schema_storage["MapCategoryType"])
    """An enumeration of several kinds of Map."""
    MarryAction = Schema(schema_storage["MarryAction"])
    """The act of marrying a person."""
    Mass = Schema(schema_storage["Mass"])
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit
    of measure&gt;'.

    E.g., '7 kg'.
    """
    MathSolver = Schema(schema_storage["MathSolver"])
    """A math solver which is capable of solving a subset of mathematical problems."""
    MaximumDoseSchedule = Schema(schema_storage["MaximumDoseSchedule"])
    """The maximum dosing schedule considered safe for a drug or supplement as
    recommended by an authority or by the drug/supplement's manufacturer.

    Capture the recommending authority in the recognizingAuthority property of
    MedicalEntity.
    """
    MayTreatHealthAspect = Schema(schema_storage["MayTreatHealthAspect"])
    """Related topics may be treated by a Topic."""
    MeasurementTypeEnumeration = Schema(schema_storage["MeasurementTypeEnumeration"])
    """Enumeration of common measurement types (or dimensions), for example "chest" for
    a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles."""
    MediaGallery = Schema(schema_storage["MediaGallery"])
    """Web page type: Media gallery page. A mixed-media page that can contains media such as images, videos, and other multimedia."""
    MediaManipulationRatingEnumeration = Schema(
        schema_storage["MediaManipulationRatingEnumeration"]
    )
    """Codes for use with the <a class="localLink"
    href="#sc.mediaAuthenticityCategory">mediaAuthenticityCategory</a> property,
    indicating the authenticity of a media object (in the context of how it was
    published or shared).

    In general these codes are not mutually exclusive, although some combinations (such
    as 'original' versus 'transformed', 'edited' and 'staged') would be contradictory if
    applied in the same <a class="localLink" href="#sc.MediaReview">MediaReview</a>.
    Note that the application of these codes is with regard to a piece of media shared
    or published in a particular context.
    """
    MediaObject = Schema(schema_storage["MediaObject"])
    """A media object, such as an image, video, or audio object embedded in a web page
    or a downloadable dataset i.e. DataDownload.

    Note that a creative work may have many media objects associated with it on the same
    web page. For example, a page about a single song (MusicRecording) may have a music
    video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).
    """
    MediaReview = Schema(schema_storage["MediaReview"])
    """A <a class="localLink" href="#sc.MediaReview">MediaReview</a> is a more
    specialized form of Review dedicated to the evaluation of media content online,
    typically in the context of fact-checking and misinformation.

    For more general reviews of media in the broader sense, use <a class="localLink" href="#sc.UserReview">UserReview</a>, <a class="localLink" href="#sc.CriticReview">CriticReview</a> or other <a class="localLink" href="#sc.Review">Review</a> types. This definition is
    a work in progress. While the <a class="localLink" href="#sc.MediaManipulationRatingEnumeration">MediaManipulationRatingEnumeration</a> list reflects significant community review amongst fact-checkers and others working
    to combat misinformation, the specific structures for representing media objects, their versions and publication context, is still evolving. Similarly, best practices for the relationship between <a class="localLink" href="#sc.MediaReview">MediaReview</a> and <a class="localLink" href="#sc.ClaimReview">ClaimReview</a> markup has not yet been finalized.
    """
    MediaSubscription = Schema(schema_storage["MediaSubscription"])
    """A subscription which allows a user to access media including audio, video, books,
    etc."""
    MedicalAudience = Schema(schema_storage["MedicalAudience"])
    """Target audiences for medical web pages."""
    MedicalAudienceType = Schema(schema_storage["MedicalAudienceType"])
    """Target audiences types for medical web pages.

    Enumerated type.
    """
    MedicalBusiness = Schema(schema_storage["MedicalBusiness"])
    """A particular physical or virtual business of an organization for medical
    purposes.

    Examples of MedicalBusiness include differents business run by health professionals.
    """
    MedicalCause = Schema(schema_storage["MedicalCause"])
    """The causative agent(s) that are responsible for the pathophysiologic process that
    eventually results in a medical condition, symptom or sign.

    In this schema, unless otherwise specified this is meant to be the proximate cause
    of the medical condition, symptom or sign. The proximate cause is defined as the
    causative agent that most directly results in the medical condition, symptom or
    sign. For example, the HIV virus could be considered a cause of AIDS. Or in a
    diagnostic context, if a patient fell and sustained a hip fracture and two days
    later sustained a pulmonary embolism which eventuated in a cardiac arrest, the cause
    of the cardiac arrest (the proximate cause) would be the pulmonary embolism and not
    the fall. Medical causes can include cardiovascular, chemical, dermatologic,
    endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic,
    iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric,
    oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal,
    rheumatologic, toxic, traumatic, or urologic causes; medical conditions can be
    causes as well.
    """
    MedicalClinic = Schema(schema_storage["MedicalClinic"])
    """A facility, often associated with a hospital or medical school, that is devoted
    to the specific diagnosis and/or healthcare.

    Previously limited to outpatients but with evolution it may be open to inpatients as
    well.
    """
    MedicalCode = Schema(schema_storage["MedicalCode"])
    """A code for a medical entity."""
    MedicalCondition = Schema(schema_storage["MedicalCondition"])
    """Any condition of the human body that affects the normal functioning of a person,
    whether physically or mentally.

    Includes diseases, injuries, disabilities, disorders, syndromes, etc.
    """
    MedicalConditionStage = Schema(schema_storage["MedicalConditionStage"])
    """A stage of a medical condition, such as 'Stage IIIa'."""
    MedicalContraindication = Schema(schema_storage["MedicalContraindication"])
    """A condition or factor that serves as a reason to withhold a certain medical
    therapy.

    Contraindications can be absolute (there are no reasonable circumstances for
    undertaking a course of action) or relative (the patient is at higher risk of
    complications, but that these risks may be outweighed by other considerations or
    mitigated by other measures).
    """
    MedicalDevice = Schema(schema_storage["MedicalDevice"])
    """Any object used in a medical capacity, such as to diagnose or treat a patient."""
    MedicalDevicePurpose = Schema(schema_storage["MedicalDevicePurpose"])
    """Categories of medical devices, organized by the purpose or intended use of the
    device."""
    MedicalEntity = Schema(schema_storage["MedicalEntity"])
    """The most generic type of entity related to health and the practice of
    medicine."""
    MedicalEnumeration = Schema(schema_storage["MedicalEnumeration"])
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice."""
    MedicalEvidenceLevel = Schema(schema_storage["MedicalEvidenceLevel"])
    """Level of evidence for a medical guideline.

    Enumerated type.
    """
    MedicalGuideline = Schema(schema_storage["MedicalGuideline"])
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus
    statement that denotes how to diagnose and treat a particular condition.

    Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.
    """
    MedicalGuidelineContraindication = Schema(
        schema_storage["MedicalGuidelineContraindication"]
    )
    """A guideline contraindication that designates a process as harmful and where
    quality of the data supporting the contraindication is sound."""
    MedicalGuidelineRecommendation = Schema(
        schema_storage["MedicalGuidelineRecommendation"]
    )
    """A guideline recommendation that is regarded as efficacious and where quality of
    the data supporting the recommendation is sound."""
    MedicalImagingTechnique = Schema(schema_storage["MedicalImagingTechnique"])
    """Any medical imaging modality typically used for diagnostic purposes.

    Enumerated type.
    """
    MedicalIndication = Schema(schema_storage["MedicalIndication"])
    """A condition or factor that indicates use of a medical therapy, including signs,
    symptoms, risk factors, anatomical states, etc."""
    MedicalIntangible = Schema(schema_storage["MedicalIntangible"])
    """A utility class that serves as the umbrella for a number of 'intangible' things
    in the medical space."""
    MedicalObservationalStudy = Schema(schema_storage["MedicalObservationalStudy"])
    """An observational study is a type of medical study that attempts to infer the
    possible effect of a treatment through observation of a cohort of subjects over a
    period of time.

    In an observational study, the assignment of subjects into treatment groups versus
    control groups is outside the control of the investigator. This is in contrast with
    controlled studies, such as the randomized controlled trials represented by
    MedicalTrial, where each subject is randomly assigned to a treatment group or a
    control group before the start of the treatment.
    """
    MedicalObservationalStudyDesign = Schema(
        schema_storage["MedicalObservationalStudyDesign"]
    )
    """Design models for observational medical studies.

    Enumerated type.
    """
    MedicalOrganization = Schema(schema_storage["MedicalOrganization"])
    """A medical organization (physical or not), such as hospital, institution or
    clinic."""
    MedicalProcedure = Schema(schema_storage["MedicalProcedure"])
    """A process of care used in either a diagnostic, therapeutic, preventive or
    palliative capacity that relies on invasive (surgical), non-invasive, or other
    techniques."""
    MedicalProcedureType = Schema(schema_storage["MedicalProcedureType"])
    """An enumeration that describes different types of medical procedures."""
    MedicalResearcher = Schema(schema_storage["MedicalResearcher"])
    """Medical researchers."""
    MedicalRiskCalculator = Schema(schema_storage["MedicalRiskCalculator"])
    """A complex mathematical calculation requiring an online calculator, used to assess
    prognosis.

    Note: use the url property of Thing to record any URLs for online calculators.
    """
    MedicalRiskEstimator = Schema(schema_storage["MedicalRiskEstimator"])
    """Any rule set or interactive tool for estimating the risk of developing a
    complication or condition."""
    MedicalRiskFactor = Schema(schema_storage["MedicalRiskFactor"])
    """A risk factor is anything that increases a person's likelihood of developing or
    contracting a disease, medical condition, or complication."""
    MedicalRiskScore = Schema(schema_storage["MedicalRiskScore"])
    """A simple system that adds up the number of risk factors to yield a score that is
    associated with prognosis, e.g. CHAD score, TIMI risk score."""
    MedicalScholarlyArticle = Schema(schema_storage["MedicalScholarlyArticle"])
    """A scholarly article in the medical domain."""
    MedicalSign = Schema(schema_storage["MedicalSign"])
    """Any physical manifestation of a person's medical condition discoverable by
    objective diagnostic tests or physical examination."""
    MedicalSignOrSymptom = Schema(schema_storage["MedicalSignOrSymptom"])
    """Any feature associated or not with a medical condition.

    In medicine a symptom is generally subjective while a sign is objective.
    """
    MedicalSpecialty = Schema(schema_storage["MedicalSpecialty"])
    """Any specific branch of medical science or practice.

    Medical specialities include clinical specialties that pertain to particular organ
    systems and their respective disease states, as well as allied health specialties.
    Enumerated type.
    """
    MedicalStudy = Schema(schema_storage["MedicalStudy"])
    """A medical study is an umbrella type covering all kinds of research studies
    relating to human medicine or health, including observational studies and
    interventional trials and registries, randomized, controlled or not.

    When the specific type of study is known, use one of the extensions of this type,
    such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should
    be used to mark up data that describes the study itself; to tag an article that
    publishes the results of a study, use MedicalScholarlyArticle. Note: use the code
    property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.
    """
    MedicalStudyStatus = Schema(schema_storage["MedicalStudyStatus"])
    """The status of a medical study.

    Enumerated type.
    """
    MedicalSymptom = Schema(schema_storage["MedicalSymptom"])
    """Any complaint sensed and expressed by the patient (therefore defined as
    subjective)  like stomachache, lower-back pain, or fatigue."""
    MedicalTest = Schema(schema_storage["MedicalTest"])
    """Any medical test, typically performed for diagnostic purposes."""
    MedicalTestPanel = Schema(schema_storage["MedicalTestPanel"])
    """Any collection of tests commonly ordered together."""
    MedicalTherapy = Schema(schema_storage["MedicalTherapy"])
    """Any medical intervention designed to prevent, treat, and cure human diseases and
    medical conditions, including both curative and palliative therapies.

    Medical therapies are typically processes of care relying upon pharmacotherapy,
    behavioral therapy, supportive therapy (with fluid or nutrition for example), or
    detoxification (e.g. hemodialysis) aimed at improving or preventing a health
    condition.
    """
    MedicalTrial = Schema(schema_storage["MedicalTrial"])
    """A medical trial is a type of medical study that uses scientific process used to
    compare the safety and efficacy of medical therapies or medical procedures.

    In general, medical trials are controlled and subjects are allocated at random to
    the different treatment and/or control groups.
    """
    MedicalTrialDesign = Schema(schema_storage["MedicalTrialDesign"])
    """Design models for medical trials.

    Enumerated type.
    """
    MedicalWebPage = Schema(schema_storage["MedicalWebPage"])
    """A web page that provides medical information."""
    MedicineSystem = Schema(schema_storage["MedicineSystem"])
    """Systems of medical practice."""
    MeetingRoom = Schema(schema_storage["MeetingRoom"])
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    MensClothingStore = Schema(schema_storage["MensClothingStore"])
    """A men's clothing store."""
    Menu = Schema(schema_storage["Menu"])
    """A structured representation of food or drink items available from a
    FoodEstablishment."""
    MenuItem = Schema(schema_storage["MenuItem"])
    """A food or drink item listed in a menu or menu section."""
    MenuSection = Schema(schema_storage["MenuSection"])
    """A sub-grouping of food or drink items in a menu.

    E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as
    'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu
    provider.
    """
    MerchantReturnEnumeration = Schema(schema_storage["MerchantReturnEnumeration"])
    """MerchantReturnEnumeration enumerates several kinds of product return policy.

    Note that this structure may not capture all aspects of the policy.
    """
    MerchantReturnFiniteReturnWindow = Schema(
        schema_storage["MerchantReturnFiniteReturnWindow"]
    )
    """MerchantReturnFiniteReturnWindow: there is a finite window for product returns."""
    MerchantReturnNotPermitted = Schema(schema_storage["MerchantReturnNotPermitted"])
    """MerchantReturnNotPermitted: product returns are not permitted."""
    MerchantReturnPolicy = Schema(schema_storage["MerchantReturnPolicy"])
    """A MerchantReturnPolicy provides information about product return policies
    associated with an <a class="localLink" href="#sc.Organization">Organization</a> or
    <a class="localLink" href="#sc.Product">Product</a>."""
    MerchantReturnUnlimitedWindow = Schema(
        schema_storage["MerchantReturnUnlimitedWindow"]
    )
    """MerchantReturnUnlimitedWindow: there is an unlimited window for product returns."""
    MerchantReturnUnspecified = Schema(schema_storage["MerchantReturnUnspecified"])
    """MerchantReturnUnspecified: a product return policy is not specified here."""
    Message = Schema(schema_storage["Message"])
    """A single message from a sender to one or more organizations or people."""
    MiddleSchool = Schema(schema_storage["MiddleSchool"])
    """A middle school (typically for children aged around 11-14, although this varies
    somewhat)."""
    Midwifery = Schema(schema_storage["Midwifery"])
    """A nurse-like health profession that deals with pregnancy, childbirth, and the
    postpartum period (including care of the newborn), besides sexual and reproductive
    health of women throughout their lives."""
    MinimumAdvertisedPrice = Schema(schema_storage["MinimumAdvertisedPrice"])
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer)
    of an offered product."""
    MisconceptionsHealthAspect = Schema(schema_storage["MisconceptionsHealthAspect"])
    """Content about common misconceptions and myths that are related to a topic."""
    MixedEventAttendanceMode = Schema(schema_storage["MixedEventAttendanceMode"])
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes."""
    MixtapeAlbum = Schema(schema_storage["MixtapeAlbum"])
    """MixtapeAlbum."""
    MobileApplication = Schema(schema_storage["MobileApplication"])
    """A software application designed specifically to work well on a mobile device such
    as a telephone."""
    MobilePhoneStore = Schema(schema_storage["MobilePhoneStore"])
    """A store that sells mobile phones and related accessories."""
    Monday = Schema(schema_storage["Monday"])
    """The day of the week between Sunday and Tuesday."""
    MonetaryAmount = Schema(schema_storage["MonetaryAmount"])
    """A monetary value or range.

    This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use <a class="localLink" href="#sc.PriceSpecification">PriceSpecification</a> Types to describe the price of an Offer, Invoice, etc.
    """
    MonetaryAmountDistribution = Schema(schema_storage["MonetaryAmountDistribution"])
    """A statistical distribution of monetary amounts."""
    MonetaryGrant = Schema(schema_storage["MonetaryGrant"])
    """A monetary grant."""
    MoneyTransfer = Schema(schema_storage["MoneyTransfer"])
    """The act of transferring money from one place to another place.

    This may occur electronically or physically.
    """
    MortgageLoan = Schema(schema_storage["MortgageLoan"])
    """A loan in which property or real estate is used as collateral.

    (A loan securitized against some real estate).
    """
    Mosque = Schema(schema_storage["Mosque"])
    """A mosque."""
    Motel = Schema(schema_storage["Motel"])
    """A motel.

    <br /><br /> See also the <a href="/docs/hotels.html">dedicated document on the use
    of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    Motorcycle = Schema(schema_storage["Motorcycle"])
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle."""
    MotorcycleDealer = Schema(schema_storage["MotorcycleDealer"])
    """A motorcycle dealer."""
    MotorcycleRepair = Schema(schema_storage["MotorcycleRepair"])
    """A motorcycle repair shop."""
    MotorizedBicycle = Schema(schema_storage["MotorizedBicycle"])
    """A motorized bicycle is a bicycle with an attached motor used to power the
    vehicle, or to assist with pedaling."""
    Mountain = Schema(schema_storage["Mountain"])
    """A mountain, like Mount Whitney or Mount Everest."""
    MoveAction = Schema(schema_storage["MoveAction"])
    """The act of an agent relocating to a place.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.TransferAction">TransferAction</a>: Unlike
    TransferAction, the subject of the move is a living Person or Organization rather
    than an inanimate object.</li> </ul>
    """
    Movie = Schema(schema_storage["Movie"])
    """A movie."""
    MovieClip = Schema(schema_storage["MovieClip"])
    """A short segment/part of a movie."""
    MovieRentalStore = Schema(schema_storage["MovieRentalStore"])
    """A movie rental store."""
    MovieSeries = Schema(schema_storage["MovieSeries"])
    """A series of movies.

    Included movies can be indicated with the hasPart property.
    """
    MovieTheater = Schema(schema_storage["MovieTheater"])
    """A movie theater."""
    MovingCompany = Schema(schema_storage["MovingCompany"])
    """A moving company."""
    MultiCenterTrial = Schema(schema_storage["MultiCenterTrial"])
    """A trial that takes place at multiple centers."""
    MultiPlayer = Schema(schema_storage["MultiPlayer"])
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously."""
    MulticellularParasite = Schema(schema_storage["MulticellularParasite"])
    """Multicellular parasite that causes an infection."""
    Muscle = Schema(schema_storage["Muscle"])
    """A muscle is an anatomical structure consisting of a contractile form of tissue
    that animals use to effect movement."""
    Musculoskeletal = Schema(schema_storage["Musculoskeletal"])
    """A specific branch of medical science that pertains to diagnosis and treatment of
    disorders of muscles, ligaments and skeletal system."""
    MusculoskeletalExam = Schema(schema_storage["MusculoskeletalExam"])
    """Musculoskeletal system clinical examination."""
    Museum = Schema(schema_storage["Museum"])
    """A museum."""
    MusicAlbum = Schema(schema_storage["MusicAlbum"])
    """A collection of music tracks."""
    MusicAlbumProductionType = Schema(schema_storage["MusicAlbumProductionType"])
    """Classification of the album by it's type of content: soundtrack, live album,
    studio album, etc."""
    MusicAlbumReleaseType = Schema(schema_storage["MusicAlbumReleaseType"])
    """The kind of release which this album is: single, EP or album."""
    MusicComposition = Schema(schema_storage["MusicComposition"])
    """A musical composition."""
    MusicEvent = Schema(schema_storage["MusicEvent"])
    """Event type: Music event."""
    MusicGroup = Schema(schema_storage["MusicGroup"])
    """A musical group, such as a band, an orchestra, or a choir.

    Can also be a solo musician.
    """
    MusicPlaylist = Schema(schema_storage["MusicPlaylist"])
    """A collection of music tracks in playlist form."""
    MusicRecording = Schema(schema_storage["MusicRecording"])
    """A music recording (track), usually a single song."""
    MusicRelease = Schema(schema_storage["MusicRelease"])
    """A MusicRelease is a specific release of a music album."""
    MusicReleaseFormatType = Schema(schema_storage["MusicReleaseFormatType"])
    """Format of this release (the type of recording media used, ie.

    compact disc, digital media, LP, etc.).
    """
    MusicStore = Schema(schema_storage["MusicStore"])
    """A music store."""
    MusicVenue = Schema(schema_storage["MusicVenue"])
    """A music venue."""
    MusicVideoObject = Schema(schema_storage["MusicVideoObject"])
    """A music video file."""
    NGO = Schema(schema_storage["NGO"])
    """Organization: Non-governmental Organization."""
    NLNonprofitType = Schema(schema_storage["NLNonprofitType"])
    """NLNonprofitType: Non-profit organization type originating from the Netherlands."""
    NailSalon = Schema(schema_storage["NailSalon"])
    """A nail salon."""
    Neck = Schema(schema_storage["Neck"])
    """Neck assessment with clinical examination."""
    Nerve = Schema(schema_storage["Nerve"])
    """A common pathway for the electrochemical nerve impulses that are transmitted
    along each of the axons."""
    Neuro = Schema(schema_storage["Neuro"])
    """Neurological system clinical examination."""
    Neurologic = Schema(schema_storage["Neurologic"])
    """A specific branch of medical science that studies the nerves and nervous system
    and its respective disease states."""
    NewCondition = Schema(schema_storage["NewCondition"])
    """Indicates that the item is new."""
    NewsArticle = Schema(schema_storage["NewsArticle"])
    """A NewsArticle is an article whose content reports news, or provides background
    context and supporting materials for understanding the news.<br/><br/>

    A more detailed overview of <a href="/docs/news.html">schema.org News markup</a> is
    also available.
    """
    NewsMediaOrganization = Schema(schema_storage["NewsMediaOrganization"])
    """A News/Media organization such as a newspaper or TV station."""
    Newspaper = Schema(schema_storage["Newspaper"])
    """A publication containing information about varied topics that are pertinent to
    general information, a geographic area, or a specific subject matter (i.e. business,
    culture, education).

    Often published daily.
    """
    NightClub = Schema(schema_storage["NightClub"])
    """A nightclub or discotheque."""
    NoninvasiveProcedure = Schema(schema_storage["NoninvasiveProcedure"])
    """A type of medical procedure that involves noninvasive techniques."""
    Nonprofit501a = Schema(schema_storage["Nonprofit501a"])
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations."""
    Nonprofit501c1 = Schema(schema_storage["Nonprofit501c1"])
    """Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations."""
    Nonprofit501c10 = Schema(schema_storage["Nonprofit501c10"])
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations."""
    Nonprofit501c11 = Schema(schema_storage["Nonprofit501c11"])
    """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations."""
    Nonprofit501c12 = Schema(schema_storage["Nonprofit501c12"])
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies."""
    Nonprofit501c13 = Schema(schema_storage["Nonprofit501c13"])
    """Nonprofit501c13: Non-profit type referring to Cemetery Companies."""
    Nonprofit501c14 = Schema(schema_storage["Nonprofit501c14"])
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds."""
    Nonprofit501c15 = Schema(schema_storage["Nonprofit501c15"])
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations."""
    Nonprofit501c16 = Schema(schema_storage["Nonprofit501c16"])
    """Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance Crop Operations."""
    Nonprofit501c17 = Schema(schema_storage["Nonprofit501c17"])
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts."""
    Nonprofit501c18 = Schema(schema_storage["Nonprofit501c18"])
    """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959)."""
    Nonprofit501c19 = Schema(schema_storage["Nonprofit501c19"])
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces."""
    Nonprofit501c2 = Schema(schema_storage["Nonprofit501c2"])
    """Nonprofit501c2: Non-profit type referring to Title-holding Corporations for Exempt Organizations."""
    Nonprofit501c20 = Schema(schema_storage["Nonprofit501c20"])
    """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations."""
    Nonprofit501c21 = Schema(schema_storage["Nonprofit501c21"])
    """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts."""
    Nonprofit501c22 = Schema(schema_storage["Nonprofit501c22"])
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds."""
    Nonprofit501c23 = Schema(schema_storage["Nonprofit501c23"])
    """Nonprofit501c23: Non-profit type referring to Veterans Organizations."""
    Nonprofit501c24 = Schema(schema_storage["Nonprofit501c24"])
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts."""
    Nonprofit501c25 = Schema(schema_storage["Nonprofit501c25"])
    """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations or Trusts with Multiple Parents."""
    Nonprofit501c26 = Schema(schema_storage["Nonprofit501c26"])
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals."""
    Nonprofit501c27 = Schema(schema_storage["Nonprofit501c27"])
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation Reinsurance Organizations."""
    Nonprofit501c28 = Schema(schema_storage["Nonprofit501c28"])
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts."""
    Nonprofit501c3 = Schema(schema_storage["Nonprofit501c3"])
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, to Foster National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations."""
    Nonprofit501c4 = Schema(schema_storage["Nonprofit501c4"])
    """Nonprofit501c4: Non-profit type referring to Civic Leagues, Social Welfare Organizations, and Local Associations of Employees."""
    Nonprofit501c5 = Schema(schema_storage["Nonprofit501c5"])
    """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations."""
    Nonprofit501c6 = Schema(schema_storage["Nonprofit501c6"])
    """Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce, Real Estate Boards."""
    Nonprofit501c7 = Schema(schema_storage["Nonprofit501c7"])
    """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs."""
    Nonprofit501c8 = Schema(schema_storage["Nonprofit501c8"])
    """Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and Associations."""
    Nonprofit501c9 = Schema(schema_storage["Nonprofit501c9"])
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations."""
    Nonprofit501d = Schema(schema_storage["Nonprofit501d"])
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations."""
    Nonprofit501e = Schema(schema_storage["Nonprofit501e"])
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations."""
    Nonprofit501f = Schema(schema_storage["Nonprofit501f"])
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations."""
    Nonprofit501k = Schema(schema_storage["Nonprofit501k"])
    """Nonprofit501k: Non-profit type referring to Child Care Organizations."""
    Nonprofit501n = Schema(schema_storage["Nonprofit501n"])
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools."""
    Nonprofit501q = Schema(schema_storage["Nonprofit501q"])
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations."""
    Nonprofit527 = Schema(schema_storage["Nonprofit527"])
    """Nonprofit527: Non-profit type referring to Political organizations."""
    NonprofitANBI = Schema(schema_storage["NonprofitANBI"])
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL)."""
    NonprofitSBBI = Schema(schema_storage["NonprofitSBBI"])
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL)."""
    NonprofitType = Schema(schema_storage["NonprofitType"])
    """NonprofitType enumerates several kinds of official non-profit types of which a
    non-profit organization can be."""
    Nose = Schema(schema_storage["Nose"])
    """Nose function assessment with clinical examination."""
    NotInForce = Schema(schema_storage["NotInForce"])
    """Indicates that a legislation is currently not in force."""
    NotYetRecruiting = Schema(schema_storage["NotYetRecruiting"])
    """Not yet recruiting."""
    Notary = Schema(schema_storage["Notary"])
    """A notary."""
    NoteDigitalDocument = Schema(schema_storage["NoteDigitalDocument"])
    """A file containing a note, primarily for the author."""
    Number = Schema(schema_storage["Number"])
    """Data type: Number.<br/><br/>

Usage guidelines:<br/><br/>

<ul>
<li>Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.</li>
<li>Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.</li>
</ul>"""
    Nursing = Schema(schema_storage["Nursing"])
    """A health profession of a person formally educated and trained in the care of the
    sick or infirm person."""
    NutritionInformation = Schema(schema_storage["NutritionInformation"])
    """Nutritional information about the recipe."""
    OTC = Schema(schema_storage["OTC"])
    """The character of a medical substance, typically a medicine, of being available
    over the counter or not."""
    Observation = Schema(schema_storage["Observation"])
    """Instances of the class <a class="localLink"
    href="#sc.Observation">Observation</a> are used to specify observations about an
    entity (which may or may not be an instance of a <a class="localLink"
    href="#sc.StatisticalPopulation">StatisticalPopulation</a>), at a particular time.

    The principal properties of an <a class="localLink" href="#sc.Observation">Observation</a> are <a class="localLink" href="#sc.observedNode">observedNode</a>, <a class="localLink" href="#sc.measuredProperty">measuredProperty</a>, <a class="localLink" href="#sc.measuredValue">measuredValue</a> (or <a class="localLink" href="#sc.median">median</a>, etc.) and <a class="localLink" href="#sc.observationDate">observationDate</a> (<a class="localLink" href="#sc.measuredProperty">measuredProperty</a> properties can, but need not always, be W3C RDF Data Cube "measure properties", as in the <a href="https://www.w3.org/TR/vocab-data-cube/#dsd-example">lifeExpectancy example</a>).
    See also <a class="localLink" href="#sc.StatisticalPopulation">StatisticalPopulation</a>, and the <a href="/docs/data-and-datasets.html">data and datasets</a> overview for more details.
    """
    Observational = Schema(schema_storage["Observational"])
    """An observational study design."""
    Obstetric = Schema(schema_storage["Obstetric"])
    """A specific branch of medical science that specializes in the care of women during
    the prenatal and postnatal care and with the delivery of the child."""
    Occupation = Schema(schema_storage["Occupation"])
    """A profession, may involve prolonged training and/or a formal qualification."""
    OccupationalActivity = Schema(schema_storage["OccupationalActivity"])
    """Any physical activity engaged in for job-related purposes.

    Examples may include waiting tables, maid service, carrying a mailbag, picking
    fruits or vegetables, construction work, etc.
    """
    OccupationalExperienceRequirements = Schema(
        schema_storage["OccupationalExperienceRequirements"]
    )
    """Indicates employment-related experience requirements, e.g. <a class="localLink"
    href="#sc.monthsOfExperience">monthsOfExperience</a>."""
    OccupationalTherapy = Schema(schema_storage["OccupationalTherapy"])
    """A treatment of people with physical, emotional, or social problems, using
    purposeful activity to help them overcome or learn to deal with their problems."""
    OceanBodyOfWater = Schema(schema_storage["OceanBodyOfWater"])
    """An ocean (for example, the Pacific)."""
    Offer = Schema(schema_storage["Offer"])
    """An offer to transfer some rights to an item or to provide a service — for
    example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream
    a TV show over the internet, to repair a motorcycle, or to loan a book.<br/><br/>

    Note: As the <a class="localLink" href="#sc.businessFunction">businessFunction</a> property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.<br/><br/>

    For <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GTIN</a>-related fields, see <a href="http://www.gs1.org/barcodes/support/check_digit_calculator">Check Digit calculator</a> and <a href="http://www.gs1us.org/resources/standards/gtin-validation-guide">validation guide</a> from <a href="http://www.gs1.org/">GS1</a>.
    """
    OfferCatalog = Schema(schema_storage["OfferCatalog"])
    """An OfferCatalog is an ItemList that contains related Offers and/or further
    OfferCatalogs that are offeredBy the same provider."""
    OfferForLease = Schema(schema_storage["OfferForLease"])
    """An <a class="localLink" href="#sc.OfferForLease">OfferForLease</a> in Schema.org represents an <a class="localLink" href="#sc.Offer">Offer</a> to lease out something, i.e. an <a class="localLink" href="#sc.Offer">Offer</a> whose
  <a class="localLink" href="#sc.businessFunction">businessFunction</a> is <a href="http://purl.org/goodrelations/v1#LeaseOut.">lease out</a>. See <a href="https://en.wikipedia.org/wiki/GoodRelations">Good Relations</a> for
  background on the underlying concepts."""
    OfferForPurchase = Schema(schema_storage["OfferForPurchase"])
    """An <a class="localLink" href="#sc.OfferForPurchase">OfferForPurchase</a> in Schema.org represents an <a class="localLink" href="#sc.Offer">Offer</a> to sell something, i.e. an <a class="localLink" href="#sc.Offer">Offer</a> whose
  <a class="localLink" href="#sc.businessFunction">businessFunction</a> is <a href="http://purl.org/goodrelations/v1#Sell.">sell</a>. See <a href="https://en.wikipedia.org/wiki/GoodRelations">Good Relations</a> for
  background on the underlying concepts."""
    OfferItemCondition = Schema(schema_storage["OfferItemCondition"])
    """A list of possible conditions for the item."""
    OfferShippingDetails = Schema(schema_storage["OfferShippingDetails"])
    """OfferShippingDetails represents information about shipping
    destinations.<br/><br/>

    Multiple of these entities can be used to represent different shipping rates for different destinations:<br/><br/>

    One entity for Alaska/Hawaii. A different one for continental US.A different one for all France.<br/><br/>

    Multiple of these entities can be used to represent different shipping costs and delivery times.<br/><br/>

    Two entities that are identical but differ in rate and time:<br/><br/>

    e.g. Cheaper and slower: $5 in 5-7days
    or Fast and expensive: $15 in 1-2 days.
    """
    OfficeEquipmentStore = Schema(schema_storage["OfficeEquipmentStore"])
    """An office equipment store."""
    OfficialLegalValue = Schema(schema_storage["OfficialLegalValue"])
    """All the documents published by an official publisher should have at least the
    legal value level "OfficialLegalValue".

    This indicates that the document was published by an organisation with the public
    task of making it available (e.g. a consolidated version of a EU directive published
    by the EU Office of Publications).
    """
    OfflineEventAttendanceMode = Schema(schema_storage["OfflineEventAttendanceMode"])
    """OfflineEventAttendanceMode - an event that is primarily conducted offline."""
    OfflinePermanently = Schema(schema_storage["OfflinePermanently"])
    """Game server status: OfflinePermanently. Server is offline and not available."""
    OfflineTemporarily = Schema(schema_storage["OfflineTemporarily"])
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon."""
    OnDemandEvent = Schema(schema_storage["OnDemandEvent"])
    """A publication event e.g. catch-up TV or radio podcast, during which a program is
    available on-demand."""
    OnSitePickup = Schema(schema_storage["OnSitePickup"])
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a
    box office."""
    Oncologic = Schema(schema_storage["Oncologic"])
    """A specific branch of medical science that deals with benign and malignant tumors,
    including the study of their development, diagnosis, treatment and prevention."""
    OneTimePayments = Schema(schema_storage["OneTimePayments"])
    """OneTimePayments: this is a benefit for one-time payments for individuals."""
    Online = Schema(schema_storage["Online"])
    """Game server status: Online. Server is available."""
    OnlineEventAttendanceMode = Schema(schema_storage["OnlineEventAttendanceMode"])
    """OnlineEventAttendanceMode - an event that is primarily conducted online."""
    OnlineFull = Schema(schema_storage["OnlineFull"])
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached."""
    OnlineOnly = Schema(schema_storage["OnlineOnly"])
    """Indicates that the item is available only online."""
    OpenTrial = Schema(schema_storage["OpenTrial"])
    """A trial design in which the researcher knows the full details of the treatment,
    and so does the patient."""
    OpeningHoursSpecification = Schema(schema_storage["OpeningHoursSpecification"])
    """A structured value providing information about the opening hours of a place or a
    certain service inside a place.<br/><br/>

    The place is <strong>open</strong> if the <a class="localLink"
    href="#sc.opens">opens</a> property is specified, and <strong>closed</strong>
    otherwise.<br/><br/>

    If the value for the <a class="localLink" href="#sc.closes">closes</a> property is
    less than the value for the <a class="localLink" href="#sc.opens">opens</a> property
    then the hour range is assumed to span over the next day.
    """
    OpinionNewsArticle = Schema(schema_storage["OpinionNewsArticle"])
    """An <a class="localLink" href="#sc.OpinionNewsArticle">OpinionNewsArticle</a> is a
    <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> that primarily expresses
    opinions rather than journalistic reporting of news and events.

    For example, a <a class="localLink" href="#sc.NewsArticle">NewsArticle</a>
    consisting of a column or <a class="localLink" href="#sc.Blog">Blog</a>/<a
    class="localLink" href="#sc.BlogPosting">BlogPosting</a> entry in the Opinions
    section of a news publication.
    """
    Optician = Schema(schema_storage["Optician"])
    """A store that sells reading glasses and similar devices for improving vision."""
    Optometric = Schema(schema_storage["Optometric"])
    """The science or practice of testing visual acuity and prescribing corrective
    lenses."""
    Order = Schema(schema_storage["Order"])
    """An order is a confirmation of a transaction (a receipt), which can contain
    multiple line items, each represented by an Offer that has been accepted by the
    customer."""
    OrderAction = Schema(schema_storage["OrderAction"])
    """An agent orders an object/product/service to be delivered/sent."""
    OrderCancelled = Schema(schema_storage["OrderCancelled"])
    """OrderStatus representing cancellation of an order."""
    OrderDelivered = Schema(schema_storage["OrderDelivered"])
    """OrderStatus representing successful delivery of an order."""
    OrderInTransit = Schema(schema_storage["OrderInTransit"])
    """OrderStatus representing that an order is in transit."""
    OrderItem = Schema(schema_storage["OrderItem"])
    """An order item is a line of an order.

    It includes the quantity and shipping details of a bought offer.
    """
    OrderPaymentDue = Schema(schema_storage["OrderPaymentDue"])
    """OrderStatus representing that payment is due on an order."""
    OrderPickupAvailable = Schema(schema_storage["OrderPickupAvailable"])
    """OrderStatus representing availability of an order for pickup."""
    OrderProblem = Schema(schema_storage["OrderProblem"])
    """OrderStatus representing that there is a problem with the order."""
    OrderProcessing = Schema(schema_storage["OrderProcessing"])
    """OrderStatus representing that an order is being processed."""
    OrderReturned = Schema(schema_storage["OrderReturned"])
    """OrderStatus representing that an order has been returned."""
    OrderStatus = Schema(schema_storage["OrderStatus"])
    """Enumerated status values for Order."""
    Organization = Schema(schema_storage["Organization"])
    """An organization such as a school, NGO, corporation, club, etc."""
    OrganizationRole = Schema(schema_storage["OrganizationRole"])
    """A subclass of Role used to describe roles within organizations."""
    OrganizeAction = Schema(schema_storage["OrganizeAction"])
    """The act of manipulating/administering/supervising/controlling one or more
    objects."""
    OriginalMediaContent = Schema(schema_storage["OriginalMediaContent"])
    """Content coded 'as original media content' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'original':
    No evidence the footage has been misleadingly altered or manipulated, though it may
    contain false or misleading claims.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be 'original':
    No evidence the image has been misleadingly altered or manipulated, though it may
    still contain false or misleading claims.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'original': No evidence the image has been misleadingly altered or
    manipulated, though it may still contain false or misleading claims.<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be 'original':
    No evidence the audio has been misleadingly altered or manipulated, though it may
    contain false or misleading claims.
    """
    OriginalShippingFees = Schema(schema_storage["OriginalShippingFees"])
    """OriginalShippingFees ..."""
    Osteopathic = Schema(schema_storage["Osteopathic"])
    """A system of medicine focused on promoting the body's innate ability to heal
    itself."""
    Otolaryngologic = Schema(schema_storage["Otolaryngologic"])
    """A specific branch of medical science that is concerned with the ear, nose and
    throat and their respective disease states."""
    OutOfStock = Schema(schema_storage["OutOfStock"])
    """Indicates that the item is out of stock."""
    OutletStore = Schema(schema_storage["OutletStore"])
    """An outlet store."""
    OverviewHealthAspect = Schema(schema_storage["OverviewHealthAspect"])
    """Overview of the content.

    Contains a summarized view of the topic with the most relevant information for an
    introduction.
    """
    OwnershipInfo = Schema(schema_storage["OwnershipInfo"])
    """A structured value providing information about when a certain organization or
    person owned a certain product."""
    PET = Schema(schema_storage["PET"])
    """Positron emission tomography imaging."""
    PaidLeave = Schema(schema_storage["PaidLeave"])
    """PaidLeave: this is a benefit for paid leave."""
    PaintAction = Schema(schema_storage["PaintAction"])
    """The act of producing a painting, typically with paint and canvas as
    instruments."""
    Painting = Schema(schema_storage["Painting"])
    """A painting."""
    PalliativeProcedure = Schema(schema_storage["PalliativeProcedure"])
    """A medical procedure intended primarily for palliative purposes, aimed at
    relieving the symptoms of an underlying health condition."""
    Paperback = Schema(schema_storage["Paperback"])
    """Book format: Paperback."""
    ParcelDelivery = Schema(schema_storage["ParcelDelivery"])
    """The delivery of a parcel either via the postal service or a commercial
    service."""
    ParcelService = Schema(schema_storage["ParcelService"])
    """A private parcel service as the delivery mode available for a certain
    offer.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#DHL</li>
    <li>http://purl.org/goodrelations/v1#FederalExpress</li>
    <li>http://purl.org/goodrelations/v1#UPS</li>
    </ul>
    """
    ParentAudience = Schema(schema_storage["ParentAudience"])
    """A set of characteristics describing parents, who can be interested in viewing
    some content."""
    ParentalSupport = Schema(schema_storage["ParentalSupport"])
    """ParentalSupport: this is a benefit for parental support."""
    Park = Schema(schema_storage["Park"])
    """A park."""
    ParkingFacility = Schema(schema_storage["ParkingFacility"])
    """A parking lot or other parking facility."""
    ParkingMap = Schema(schema_storage["ParkingMap"])
    """A parking map."""
    PartiallyInForce = Schema(schema_storage["PartiallyInForce"])
    """Indicates that parts of the legislation are in force, and parts are not."""
    Pathology = Schema(schema_storage["Pathology"])
    """A specific branch of medical science that is concerned with the study of the
    cause, origin and nature of a disease state, including its consequences as a result
    of manifestation of the disease.

    In clinical care, the term is used to designate a branch of medicine using
    laboratory tests to diagnose and determine the prognostic significance of illness.
    """
    PathologyTest = Schema(schema_storage["PathologyTest"])
    """A medical test performed by a laboratory that typically involves examination of a
    tissue sample by a pathologist."""
    Patient = Schema(schema_storage["Patient"])
    """A patient is any person recipient of health care services."""
    PatientExperienceHealthAspect = Schema(
        schema_storage["PatientExperienceHealthAspect"]
    )
    """Content about the real life experience of patients or people that have lived a
    similar experience about the topic.

    May be forums, topics, Q-and-A and related material.
    """
    PawnShop = Schema(schema_storage["PawnShop"])
    """A shop that will buy, or lend money against the security of, personal
    possessions."""
    PayAction = Schema(schema_storage["PayAction"])
    """An agent pays a price to a participant."""
    PaymentAutomaticallyApplied = Schema(schema_storage["PaymentAutomaticallyApplied"])
    """An automatic payment system is in place and will be used."""
    PaymentCard = Schema(schema_storage["PaymentCard"])
    """A payment method using a credit, debit, store or other card to associate the
    payment with an account."""
    PaymentChargeSpecification = Schema(schema_storage["PaymentChargeSpecification"])
    """The costs of settling the payment using a particular payment method."""
    PaymentComplete = Schema(schema_storage["PaymentComplete"])
    """The payment has been received and processed."""
    PaymentDeclined = Schema(schema_storage["PaymentDeclined"])
    """The payee received the payment, but it was declined for some reason."""
    PaymentDue = Schema(schema_storage["PaymentDue"])
    """The payment is due, but still within an acceptable time to be received."""
    PaymentMethod = Schema(schema_storage["PaymentMethod"])
    """A payment method is a standardized procedure for transferring the monetary amount
    for a purchase. Payment methods are characterized by the legal and technical
    structures used, and by the organization or group carrying out the
    transaction.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#ByBankTransferInAdvance</li>
    <li>http://purl.org/goodrelations/v1#ByInvoice</li>
    <li>http://purl.org/goodrelations/v1#Cash</li>
    <li>http://purl.org/goodrelations/v1#CheckInAdvance</li>
    <li>http://purl.org/goodrelations/v1#COD</li>
    <li>http://purl.org/goodrelations/v1#DirectDebit</li>
    <li>http://purl.org/goodrelations/v1#GoogleCheckout</li>
    <li>http://purl.org/goodrelations/v1#PayPal</li>
    <li>http://purl.org/goodrelations/v1#PaySwarm</li>
    </ul>
    """
    PaymentPastDue = Schema(schema_storage["PaymentPastDue"])
    """The payment is due and considered late."""
    PaymentService = Schema(schema_storage["PaymentService"])
    """A Service to transfer funds from a person or organization to a beneficiary person
    or organization."""
    PaymentStatusType = Schema(schema_storage["PaymentStatusType"])
    """A specific payment status.

    For example, PaymentDue, PaymentComplete, etc.
    """
    Pediatric = Schema(schema_storage["Pediatric"])
    """A specific branch of medical science that specializes in the care of infants,
    children and adolescents."""
    PeopleAudience = Schema(schema_storage["PeopleAudience"])
    """A set of characteristics belonging to people, e.g. who compose an item's target
    audience."""
    PercutaneousProcedure = Schema(schema_storage["PercutaneousProcedure"])
    """A type of medical procedure that involves percutaneous techniques, where access
    to organs or tissue is achieved via needle-puncture of the skin.

    For example, catheter-based procedures like stent delivery.
    """
    PerformAction = Schema(schema_storage["PerformAction"])
    """The act of participating in performance arts."""
    PerformanceRole = Schema(schema_storage["PerformanceRole"])
    """A PerformanceRole is a Role that some entity places with regard to a theatrical
    performance, e.g. in a Movie, TVSeries etc."""
    PerformingArtsTheater = Schema(schema_storage["PerformingArtsTheater"])
    """A theater or other performing art center."""
    PerformingGroup = Schema(schema_storage["PerformingGroup"])
    """A performance group, such as a band, an orchestra, or a circus."""
    Periodical = Schema(schema_storage["Periodical"])
    """A publication in any medium issued in successive parts bearing numerical or
    chronological designations and intended, such as a magazine, scholarly journal, or
    newspaper to continue indefinitely.<br/><br/>

    See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.
    """
    Permit = Schema(schema_storage["Permit"])
    """A permit issued by an organization, e.g. a parking pass."""
    Person = Schema(schema_storage["Person"])
    """A person (alive, dead, undead, or fictional)."""
    PetStore = Schema(schema_storage["PetStore"])
    """A pet store."""
    Pharmacy = Schema(schema_storage["Pharmacy"])
    """A pharmacy or drugstore."""
    PharmacySpecialty = Schema(schema_storage["PharmacySpecialty"])
    """The practice or art and science of preparing and dispensing drugs and
    medicines."""
    Photograph = Schema(schema_storage["Photograph"])
    """A photograph."""
    PhotographAction = Schema(schema_storage["PhotographAction"])
    """The act of capturing still images of objects using a camera."""
    PhysicalActivity = Schema(schema_storage["PhysicalActivity"])
    """Any bodily activity that enhances or maintains physical fitness and overall
    health and wellness.

    Includes activity that is part of daily living and routine, structured exercise, and
    exercise prescribed as part of a medical treatment or recovery plan.
    """
    PhysicalActivityCategory = Schema(schema_storage["PhysicalActivityCategory"])
    """Categories of physical activity, organized by physiologic classification."""
    PhysicalExam = Schema(schema_storage["PhysicalExam"])
    """A type of physical examination of a patient performed by a physician."""
    PhysicalTherapy = Schema(schema_storage["PhysicalTherapy"])
    """A process of progressive physical care and rehabilitation aimed at improving a
    health condition."""
    Physician = Schema(schema_storage["Physician"])
    """A doctor's office."""
    Physiotherapy = Schema(schema_storage["Physiotherapy"])
    """The practice of treatment of disease, injury, or deformity by physical methods
    such as massage, heat treatment, and exercise rather than by drugs or surgery.."""
    Place = Schema(schema_storage["Place"])
    """Entities that have a somewhat fixed, physical extension."""
    PlaceOfWorship = Schema(schema_storage["PlaceOfWorship"])
    """Place of worship, such as a church, synagogue, or mosque."""
    PlaceboControlledTrial = Schema(schema_storage["PlaceboControlledTrial"])
    """A placebo-controlled trial design."""
    PlanAction = Schema(schema_storage["PlanAction"])
    """The act of planning the execution of an event/task/action/reservation/plan to a
    future date."""
    PlasticSurgery = Schema(schema_storage["PlasticSurgery"])
    """A specific branch of medical science that pertains to therapeutic or cosmetic
    repair or re-formation of missing, injured or malformed tissues or body parts by
    manual and instrumental means."""
    Play = Schema(schema_storage["Play"])
    """A play is a form of literature, usually consisting of dialogue between
    characters, intended for theatrical performance rather than just reading.

    Note the peformance of a Play would be a <a class="localLink" href="#sc.TheaterEvent">TheaterEvent</a> - the <em>Play</em> being the <a class="localLink" href="#sc.workPerformed">workPerformed</a>.
    """
    PlayAction = Schema(schema_storage["PlayAction"])
    """The act of playing/exercising/training/performing for enjoyment, leisure,
    recreation, Competition or exercise.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ListenAction">ListenAction</a>: Unlike
    ListenAction (which is under ConsumeAction), PlayAction refers to performing for an
    audience or at an event, rather than consuming music.</li> <li><a class="localLink"
    href="#sc.WatchAction">WatchAction</a>: Unlike WatchAction (which is under
    ConsumeAction), PlayAction refers to showing/displaying for an audience or at an
    event, rather than consuming visual content.</li> </ul>
    """
    Playground = Schema(schema_storage["Playground"])
    """A playground."""
    Plumber = Schema(schema_storage["Plumber"])
    """A plumbing service."""
    PodcastEpisode = Schema(schema_storage["PodcastEpisode"])
    """A single episode of a podcast series."""
    PodcastSeason = Schema(schema_storage["PodcastSeason"])
    """A single season of a podcast.

    Many podcasts do not break down into separate seasons. In that case, PodcastSeries
    should be used.
    """
    PodcastSeries = Schema(schema_storage["PodcastSeries"])
    """A podcast is an episodic series of digital audio or video files which a user can
    download and listen to."""
    Podiatric = Schema(schema_storage["Podiatric"])
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of
    foot disorders."""
    PoliceStation = Schema(schema_storage["PoliceStation"])
    """A police station."""
    Pond = Schema(schema_storage["Pond"])
    """A pond."""
    PostOffice = Schema(schema_storage["PostOffice"])
    """A post office."""
    PostalAddress = Schema(schema_storage["PostalAddress"])
    """The mailing address."""
    PostalCodeRangeSpecification = Schema(
        schema_storage["PostalCodeRangeSpecification"]
    )
    """Indicates a range of postalcodes, usually defined as the set of valid codes
    between <a class="localLink" href="#sc.postalCodeBegin">postalCodeBegin</a> and <a
    class="localLink" href="#sc.postalCodeEnd">postalCodeEnd</a>, inclusively."""
    Poster = Schema(schema_storage["Poster"])
    """A large, usually printed placard, bill, or announcement, often illustrated, that
    is posted to advertise or publicize something."""
    PotentialActionStatus = Schema(schema_storage["PotentialActionStatus"])
    """A description of an action that is supported."""
    PreOrder = Schema(schema_storage["PreOrder"])
    """Indicates that the item is available for pre-order."""
    PreOrderAction = Schema(schema_storage["PreOrderAction"])
    """An agent orders a (not yet released) object/product/service to be
    delivered/sent."""
    PreSale = Schema(schema_storage["PreSale"])
    """Indicates that the item is available for ordering and delivery before general
    availability."""
    PregnancyHealthAspect = Schema(schema_storage["PregnancyHealthAspect"])
    """Content discussing pregnancy-related aspects of a health topic."""
    PrependAction = Schema(schema_storage["PrependAction"])
    """The act of inserting at the beginning if an ordered collection."""
    Preschool = Schema(schema_storage["Preschool"])
    """A preschool."""
    PrescriptionOnly = Schema(schema_storage["PrescriptionOnly"])
    """Available by prescription only."""
    PresentationDigitalDocument = Schema(schema_storage["PresentationDigitalDocument"])
    """A file containing slides or used for a presentation."""
    PreventionHealthAspect = Schema(schema_storage["PreventionHealthAspect"])
    """Information about actions or measures that can be taken to avoid getting the
    topic or reaching a critical situation related to the topic."""
    PreventionIndication = Schema(schema_storage["PreventionIndication"])
    """An indication for preventing an underlying condition, symptom, etc."""
    PriceComponentTypeEnumeration = Schema(
        schema_storage["PriceComponentTypeEnumeration"]
    )
    """Enumerates different price components that together make up the total price for
    an offered product."""
    PriceSpecification = Schema(schema_storage["PriceSpecification"])
    """A structured value representing a price or price range.

    Typically, only the subclasses of this type are used for markup. It is recommended
    to use <a class="localLink" href="#sc.MonetaryAmount">MonetaryAmount</a> to describe
    independent amounts of money such as a salary, credit card limits, etc.
    """
    PriceTypeEnumeration = Schema(schema_storage["PriceTypeEnumeration"])
    """Enumerates different price types, for example list price, invoice price, and sale
    price."""
    PrimaryCare = Schema(schema_storage["PrimaryCare"])
    """The medical care by a physician, or other health-care professional, who is the
    patient's first contact with the health-care system and who may recommend a
    specialist if necessary."""
    Prion = Schema(schema_storage["Prion"])
    """A prion is an infectious agent composed of protein in a misfolded form."""
    Product = Schema(schema_storage["Product"])
    """Any offered product or service.

    For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """
    ProductCollection = Schema(schema_storage["ProductCollection"])
    """A set of products (either <a class="localLink"
    href="#sc.ProductGroup">ProductGroup</a>s or specific variants) that are listed
    together e.g. in an <a class="localLink" href="#sc.Offer">Offer</a>."""
    ProductGroup = Schema(schema_storage["ProductGroup"])
    """A ProductGroup represents a group of <a class="localLink"
    href="#sc.Product">Product</a>s that vary only in certain well-described ways, such
    as by <a class="localLink" href="#sc.size">size</a>, <a class="localLink"
    href="#sc.color">color</a>, <a class="localLink" href="#sc.material">material</a>
    etc.<br/><br/>

    While a ProductGroup itself is not directly offered for sale, the various varying
    products that it represents can be. The ProductGroup serves as a prototype or
    template, standing in for all of the products who have an <a class="localLink"
    href="#sc.isVariantOf">isVariantOf</a> relationship to it. As such, properties
    (including additional types) can be applied to the ProductGroup to represent
    characteristics shared by each of the (possibly very many) variants. Properties that
    reference a ProductGroup are not included in this mechanism; neither are the
    following specific properties <a class="localLink" href="#sc.variesBy">variesBy</a>,
    <a class="localLink" href="#sc.hasVariant">hasVariant</a>, <a class="localLink"
    href="#sc.url">url</a>.
    """
    ProductModel = Schema(schema_storage["ProductModel"])
    """A datasheet or vendor specification of a product (in the sense of a prototypical
    description)."""
    ProductReturnEnumeration = Schema(schema_storage["ProductReturnEnumeration"])
    """ProductReturnEnumeration enumerates several kinds of product return policy.

    Note that this structure may not capture all aspects of the policy.
    """
    ProductReturnFiniteReturnWindow = Schema(
        schema_storage["ProductReturnFiniteReturnWindow"]
    )
    """ProductReturnFiniteReturnWindow: there is a finite window for product returns."""
    ProductReturnNotPermitted = Schema(schema_storage["ProductReturnNotPermitted"])
    """ProductReturnNotPermitted: product returns are not permitted."""
    ProductReturnPolicy = Schema(schema_storage["ProductReturnPolicy"])
    """A ProductReturnPolicy provides information about product return policies
    associated with an <a class="localLink" href="#sc.Organization">Organization</a> or
    <a class="localLink" href="#sc.Product">Product</a>."""
    ProductReturnUnlimitedWindow = Schema(
        schema_storage["ProductReturnUnlimitedWindow"]
    )
    """ProductReturnUnlimitedWindow: there is an unlimited window for product returns."""
    ProductReturnUnspecified = Schema(schema_storage["ProductReturnUnspecified"])
    """ProductReturnUnspecified: a product return policy is not specified here."""
    ProfessionalService = Schema(schema_storage["ProfessionalService"])
    """Original definition: "provider of professional services."<br/><br/>

The general <a class="localLink" href="#sc.ProfessionalService">ProfessionalService</a> type for local businesses was deprecated due to confusion with <a class="localLink" href="#sc.Service">Service</a>. For reference, the types that it included were: <a class="localLink" href="#sc.Dentist">Dentist</a>,
        <a class="localLink" href="#sc.AccountingService">AccountingService</a>, <a class="localLink" href="#sc.Attorney">Attorney</a>, <a class="localLink" href="#sc.Notary">Notary</a>, as well as types for several kinds of <a class="localLink" href="#sc.HomeAndConstructionBusiness">HomeAndConstructionBusiness</a>: <a class="localLink" href="#sc.Electrician">Electrician</a>, <a class="localLink" href="#sc.GeneralContractor">GeneralContractor</a>,
        <a class="localLink" href="#sc.HousePainter">HousePainter</a>, <a class="localLink" href="#sc.Locksmith">Locksmith</a>, <a class="localLink" href="#sc.Plumber">Plumber</a>, <a class="localLink" href="#sc.RoofingContractor">RoofingContractor</a>. <a class="localLink" href="#sc.LegalService">LegalService</a> was introduced as a more inclusive supertype of <a class="localLink" href="#sc.Attorney">Attorney</a>."""
    ProfilePage = Schema(schema_storage["ProfilePage"])
    """Web page type: Profile page."""
    PrognosisHealthAspect = Schema(schema_storage["PrognosisHealthAspect"])
    """Typical progression and happenings of life course of the topic."""
    ProgramMembership = Schema(schema_storage["ProgramMembership"])
    """Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler
    clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc."""
    Project = Schema(schema_storage["Project"])
    """An enterprise (potentially individual but typically collaborative), planned to
    achieve a particular aim.

    Use properties from <a class="localLink" href="#sc.Organization">Organization</a>, <a class="localLink" href="#sc.subOrganization">subOrganization</a>/<a class="localLink" href="#sc.parentOrganization">parentOrganization</a> to indicate project sub-structures.
    """
    PronounceableText = Schema(schema_storage["PronounceableText"])
    """Data type: PronounceableText."""
    Property = Schema(schema_storage["Property"])
    """A property, used to indicate attributes and relationships of some Thing;
    equivalent to rdf:Property."""
    PropertyValue = Schema(schema_storage["PropertyValue"])
    """A property-value pair, e.g. representing a feature of a product or place. Use the
    'name' property for the name of the property. If there is an additional human-
    readable version of the value, put that into the 'description' property.<br/><br/>

    Always use specific schema.org properties when a) they exist and b) you can populate
    them. Using PropertyValue as a substitute will typically not trigger the same effect
    as using the original, specific property.
    """
    PropertyValueSpecification = Schema(schema_storage["PropertyValueSpecification"])
    """A Property value specification."""
    Protozoa = Schema(schema_storage["Protozoa"])
    """Single-celled organism that causes an infection."""
    Psychiatric = Schema(schema_storage["Psychiatric"])
    """A specific branch of medical science that is concerned with the study, treatment,
    and prevention of mental illness, using both medical and psychological therapies."""
    PsychologicalTreatment = Schema(schema_storage["PsychologicalTreatment"])
    """A process of care relying upon counseling, dialogue and communication  aimed at
    improving a mental health condition without use of drugs."""
    PublicHealth = Schema(schema_storage["PublicHealth"])
    """Branch of medicine that pertains to the health services to improve and protect
    community health, especially epidemiology, sanitation, immunization, and preventive
    medicine."""
    PublicHolidays = Schema(schema_storage["PublicHolidays"])
    """This stands for any day that is a public holiday; it is a placeholder for all
    official public holidays in some particular location.

    While not technically a "day of the week", it can be used with <a class="localLink" href="#sc.OpeningHoursSpecification">OpeningHoursSpecification</a>. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.
    """
    PublicSwimmingPool = Schema(schema_storage["PublicSwimmingPool"])
    """A public swimming pool."""
    PublicToilet = Schema(schema_storage["PublicToilet"])
    """A public toilet is a room or small building containing one or more toilets (and
    possibly also urinals) which is available for use by the general public, or by
    customers or employees of certain businesses."""
    PublicationEvent = Schema(schema_storage["PublicationEvent"])
    """A PublicationEvent corresponds indifferently to the event of publication for a
    CreativeWork of any type e.g. a broadcast event, an on-demand event, a book/journal
    publication via a variety of delivery media."""
    PublicationIssue = Schema(schema_storage["PublicationIssue"])
    """A part of a successively published publication such as a periodical or
    publication volume, often numbered, usually containing a grouping of works such as
    articles.<br/><br/>

    See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.
    """
    PublicationVolume = Schema(schema_storage["PublicationVolume"])
    """A part of a successively published publication such as a periodical or multi-
    volume work, often numbered. It may represent a time span, such as a year.<br/><br/>

    See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.
    """
    Pulmonary = Schema(schema_storage["Pulmonary"])
    """A specific branch of medical science that pertains to the study of the
    respiratory system and its respective disease states."""
    QAPage = Schema(schema_storage["QAPage"])
    """A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in
    a question answering site or documenting Frequently Asked Questions (FAQs)."""
    QualitativeValue = Schema(schema_storage["QualitativeValue"])
    """A predefined value for a product characteristic, e.g. the power cord plug type
    'US' or the garment sizes 'S', 'M', 'L', and 'XL'."""
    QuantitativeValue = Schema(schema_storage["QuantitativeValue"])
    """A point value or interval for product characteristics and other purposes."""
    QuantitativeValueDistribution = Schema(
        schema_storage["QuantitativeValueDistribution"]
    )
    """A statistical distribution of values."""
    Quantity = Schema(schema_storage["Quantity"])
    """Quantities such as distance, time, mass, weight, etc.

    Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.
    """
    Question = Schema(schema_storage["Question"])
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document."""
    Quiz = Schema(schema_storage["Quiz"])
    """Quiz: A test of knowledge, skills and abilities."""
    Quotation = Schema(schema_storage["Quotation"])
    """A quotation.

    Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use <a class="localLink" href="#sc.isBasedOn">isBasedOn</a> to link to source/origin. The <a class="localLink" href="#sc.recordedIn">recordedIn</a> property can be used to reference a Quotation from an <a class="localLink" href="#sc.Event">Event</a>.
    """
    QuoteAction = Schema(schema_storage["QuoteAction"])
    """An agent quotes/estimates/appraises an object/product/service with a price at a
    location/store."""
    RVPark = Schema(schema_storage["RVPark"])
    """A place offering space for "Recreational Vehicles", Caravans, mobile homes and
    the like."""
    RadiationTherapy = Schema(schema_storage["RadiationTherapy"])
    """A process of care using radiation aimed at improving a health condition."""
    RadioBroadcastService = Schema(schema_storage["RadioBroadcastService"])
    """A delivery service through which radio content is provided via broadcast over the
    air or online."""
    RadioChannel = Schema(schema_storage["RadioChannel"])
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService
    lineup."""
    RadioClip = Schema(schema_storage["RadioClip"])
    """A short radio program or a segment/part of a radio program."""
    RadioEpisode = Schema(schema_storage["RadioEpisode"])
    """A radio episode which can be part of a series or season."""
    RadioSeason = Schema(schema_storage["RadioSeason"])
    """Season dedicated to radio broadcast and associated online delivery."""
    RadioSeries = Schema(schema_storage["RadioSeries"])
    """CreativeWorkSeries dedicated to radio broadcast and associated online
    delivery."""
    RadioStation = Schema(schema_storage["RadioStation"])
    """A radio station."""
    Radiography = Schema(schema_storage["Radiography"])
    """Radiography is an imaging technique that uses electromagnetic radiation other
    than visible light, especially X-rays, to view the internal structure of a non-
    uniformly composed and opaque object such as the human body."""
    RandomizedTrial = Schema(schema_storage["RandomizedTrial"])
    """A randomized trial design."""
    Rating = Schema(schema_storage["Rating"])
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars."""
    ReactAction = Schema(schema_storage["ReactAction"])
    """The act of responding instinctively and emotionally to an object, expressing a
    sentiment."""
    ReadAction = Schema(schema_storage["ReadAction"])
    """The act of consuming written content."""
    ReadPermission = Schema(schema_storage["ReadPermission"])
    """Permission to read or view the document."""
    RealEstateAgent = Schema(schema_storage["RealEstateAgent"])
    """A real-estate agent."""
    RealEstateListing = Schema(schema_storage["RealEstateListing"])
    """A <a class="localLink" href="#sc.RealEstateListing">RealEstateListing</a> is a
    listing that describes one or more real-estate <a class="localLink"
    href="#sc.Offer">Offer</a>s (whose <a class="localLink"
    href="#sc.businessFunction">businessFunction</a> is typically to lease out, or to
    sell).

    The <a class="localLink" href="#sc.RealEstateListing">RealEstateListing</a> type
    itself represents the overall listing, as manifested in some <a class="localLink"
    href="#sc.WebPage">WebPage</a>.
    """
    RearWheelDriveConfiguration = Schema(schema_storage["RearWheelDriveConfiguration"])
    """Real-wheel drive is a transmission layout where the engine drives the rear
    wheels."""
    ReceiveAction = Schema(schema_storage["ReceiveAction"])
    """The act of physically/electronically taking delivery of an object that has been
    transferred from an origin to a destination. Reciprocal of SendAction.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.SendAction">SendAction</a>: The reciprocal
    of ReceiveAction.</li> <li><a class="localLink"
    href="#sc.TakeAction">TakeAction</a>: Unlike TakeAction, ReceiveAction does not
    imply that the ownership has been transfered (e.g. I can receive a package, but it
    does not mean the package is now mine).</li> </ul>
    """
    Recipe = Schema(schema_storage["Recipe"])
    """A recipe.

    For dietary restrictions covered by the recipe, a few common restrictions are
    enumerated via <a class="localLink" href="#sc.suitableForDiet">suitableForDiet</a>.
    The <a class="localLink" href="#sc.keywords">keywords</a> property can also be used
    to add more detail.
    """
    Recommendation = Schema(schema_storage["Recommendation"])
    """<a class="localLink" href="#sc.Recommendation">Recommendation</a> is a type of <a
    class="localLink" href="#sc.Review">Review</a> that suggests or proposes something
    as the best option or best course of action.

    Recommendations may be for products or services, or other concrete things, as in the
    case of a ranked list or product guide. A <a class="localLink"
    href="#sc.Guide">Guide</a> may list multiple recommendations for different
    categories. For example, in a <a class="localLink" href="#sc.Guide">Guide</a> about
    which TVs to buy, the author may have several <a class="localLink"
    href="#sc.Recommendation">Recommendation</a>s.
    """
    RecommendedDoseSchedule = Schema(schema_storage["RecommendedDoseSchedule"])
    """A recommended dosing schedule for a drug or supplement as prescribed or
    recommended by an authority or by the drug/supplement's manufacturer.

    Capture the recommending authority in the recognizingAuthority property of
    MedicalEntity.
    """
    Recruiting = Schema(schema_storage["Recruiting"])
    """Recruiting participants."""
    RecyclingCenter = Schema(schema_storage["RecyclingCenter"])
    """A recycling center."""
    RefundTypeEnumeration = Schema(schema_storage["RefundTypeEnumeration"])
    """RefundTypeEnumeration enumerates several kinds of product return refund types."""
    RefurbishedCondition = Schema(schema_storage["RefurbishedCondition"])
    """Indicates that the item is refurbished."""
    RegisterAction = Schema(schema_storage["RegisterAction"])
    """The act of registering to be a user of a service, product or web page.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.JoinAction">JoinAction</a>: Unlike
    JoinAction, RegisterAction implies you are registering to be a user of a service,
    <em>not</em> a group/team of people.</li> <li>[FollowAction]]: Unlike FollowAction,
    RegisterAction doesn't imply that the agent is expecting to poll for updates from
    the object.</li> <li><a class="localLink"
    href="#sc.SubscribeAction">SubscribeAction</a>: Unlike SubscribeAction,
    RegisterAction doesn't imply that the agent is expecting updates from the
    object.</li> </ul>
    """
    Registry = Schema(schema_storage["Registry"])
    """A registry-based study design."""
    ReimbursementCap = Schema(schema_storage["ReimbursementCap"])
    """The drug's cost represents the maximum reimbursement paid by an insurer for the
    drug."""
    RejectAction = Schema(schema_storage["RejectAction"])
    """The act of rejecting to/adopting an object.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.AcceptAction">AcceptAction</a>: The antonym
    of RejectAction.</li> </ul>
    """
    RelatedTopicsHealthAspect = Schema(schema_storage["RelatedTopicsHealthAspect"])
    """Other prominent or relevant topics tied to the main topic."""
    RemixAlbum = Schema(schema_storage["RemixAlbum"])
    """RemixAlbum."""
    Renal = Schema(schema_storage["Renal"])
    """A specific branch of medical science that pertains to the study of the kidneys
    and its respective disease states."""
    RentAction = Schema(schema_storage["RentAction"])
    """The act of giving money in return for temporary use, but not ownership, of an
    object such as a vehicle or property.

    For example, an agent rents a property from a landlord in exchange for a periodic
    payment.
    """
    RentalCarReservation = Schema(schema_storage["RentalCarReservation"])
    """A reservation for a rental car.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.
    """
    RentalVehicleUsage = Schema(schema_storage["RentalVehicleUsage"])
    """Indicates the usage of the vehicle as a rental car."""
    RepaymentSpecification = Schema(schema_storage["RepaymentSpecification"])
    """A structured value representing repayment."""
    ReplaceAction = Schema(schema_storage["ReplaceAction"])
    """The act of editing a recipient by replacing an old object with a new object."""
    ReplyAction = Schema(schema_storage["ReplyAction"])
    """The act of responding to a question/message asked/sent by the object. Related to
    <a class="localLink" href="#sc.AskAction">AskAction</a><br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.AskAction">AskAction</a>: Appears generally
    as an origin of a ReplyAction.</li> </ul>
    """
    Report = Schema(schema_storage["Report"])
    """A Report generated by governmental or non-governmental organization."""
    ReportageNewsArticle = Schema(schema_storage["ReportageNewsArticle"])
    """The <a class="localLink" href="#sc.ReportageNewsArticle">ReportageNewsArticle</a>
    type is a subtype of <a class="localLink" href="#sc.NewsArticle">NewsArticle</a>
    representing news articles which are the result of journalistic news reporting
    conventions.<br/><br/>

    In practice many news publishers produce a wide variety of article types, many of which might be considered a <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> but not a <a class="localLink" href="#sc.ReportageNewsArticle">ReportageNewsArticle</a>. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.<br/><br/>

    The <a class="localLink" href="#sc.ReportageNewsArticle">ReportageNewsArticle</a> type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the <a class="localLink" href="#sc.ReportageNewsArticle">ReportageNewsArticle</a> sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.<br/><br/>

    A <a class="localLink" href="#sc.ReportageNewsArticle">ReportageNewsArticle</a> which goes deeper into analysis can also be marked with an additional type of <a class="localLink" href="#sc.AnalysisNewsArticle">AnalysisNewsArticle</a>.
    """
    ReportedDoseSchedule = Schema(schema_storage["ReportedDoseSchedule"])
    """A patient-reported or observed dosing schedule for a drug or supplement."""
    ResearchProject = Schema(schema_storage["ResearchProject"])
    """A Research project."""
    Researcher = Schema(schema_storage["Researcher"])
    """Researchers."""
    Reservation = Schema(schema_storage["Reservation"])
    """Describes a reservation for travel, dining or an event. Some reservations require
    tickets. <br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    ReservationCancelled = Schema(schema_storage["ReservationCancelled"])
    """The status for a previously confirmed reservation that is now cancelled."""
    ReservationConfirmed = Schema(schema_storage["ReservationConfirmed"])
    """The status of a confirmed reservation."""
    ReservationHold = Schema(schema_storage["ReservationHold"])
    """The status of a reservation on hold pending an update like credit card number or
    flight changes."""
    ReservationPackage = Schema(schema_storage["ReservationPackage"])
    """A group of multiple reservations with common values for all sub-reservations."""
    ReservationPending = Schema(schema_storage["ReservationPending"])
    """The status of a reservation when a request has been sent, but not confirmed."""
    ReservationStatusType = Schema(schema_storage["ReservationStatusType"])
    """Enumerated status values for Reservation."""
    ReserveAction = Schema(schema_storage["ReserveAction"])
    """Reserving a concrete object.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ScheduleAction">ScheduleAction</a>: Unlike
    ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel)
    towards a time slot / spatial allocation.</li> </ul>
    """
    Reservoir = Schema(schema_storage["Reservoir"])
    """A reservoir of water, typically an artificially created lake, like the Lake
    Kariba reservoir."""
    Residence = Schema(schema_storage["Residence"])
    """The place where a person lives."""
    Resort = Schema(schema_storage["Resort"])
    """A resort is a place used for relaxation or recreation, attracting visitors for
    holidays or vacations.

    Resorts are places, towns or sometimes commercial establishment operated by a single company (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Resort">http://en.wikipedia.org/wiki/Resort</a>).
    <br /><br />
    See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    RespiratoryTherapy = Schema(schema_storage["RespiratoryTherapy"])
    """The therapy that is concerned with the maintenance or improvement of respiratory
    function (as in patients with pulmonary disease)."""
    Restaurant = Schema(schema_storage["Restaurant"])
    """A restaurant."""
    RestockingFees = Schema(schema_storage["RestockingFees"])
    """RestockingFees ..."""
    RestrictedDiet = Schema(schema_storage["RestrictedDiet"])
    """A diet restricted to certain foods or preparations for cultural, religious,
    health or lifestyle reasons."""
    ResultsAvailable = Schema(schema_storage["ResultsAvailable"])
    """Results are available."""
    ResultsNotAvailable = Schema(schema_storage["ResultsNotAvailable"])
    """Results are not available."""
    ResumeAction = Schema(schema_storage["ResumeAction"])
    """The act of resuming a device or application which was formerly paused (e.g.
    resume music playback or resume a timer)."""
    Retail = Schema(schema_storage["Retail"])
    """The drug's cost represents the retail cost of the drug."""
    ReturnAction = Schema(schema_storage["ReturnAction"])
    """The act of returning to the origin that which was previously received (concrete
    objects) or taken (ownership)."""
    ReturnFeesEnumeration = Schema(schema_storage["ReturnFeesEnumeration"])
    """ReturnFeesEnumeration expresses policies for return fees."""
    ReturnShippingFees = Schema(schema_storage["ReturnShippingFees"])
    """ReturnShippingFees ..."""
    Review = Schema(schema_storage["Review"])
    """A review of an item - for example, of a restaurant, movie, or store."""
    ReviewAction = Schema(schema_storage["ReviewAction"])
    """The act of producing a balanced opinion about the object for an audience.

    An agent reviews an object with participants resulting in a review.
    """
    ReviewNewsArticle = Schema(schema_storage["ReviewNewsArticle"])
    """A <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> and <a
    class="localLink" href="#sc.CriticReview">CriticReview</a> providing a professional
    critic's assessment of a service, product, performance, or artistic or literary
    work."""
    Rheumatologic = Schema(schema_storage["Rheumatologic"])
    """A specific branch of medical science that deals with the study and treatment of
    rheumatic, autoimmune or joint diseases."""
    RightHandDriving = Schema(schema_storage["RightHandDriving"])
    """The steering position is on the right side of the vehicle (viewed from the main
    direction of driving)."""
    RisksOrComplicationsHealthAspect = Schema(
        schema_storage["RisksOrComplicationsHealthAspect"]
    )
    """Information about the risk factors and possible complications that may follow a
    topic."""
    RiverBodyOfWater = Schema(schema_storage["RiverBodyOfWater"])
    """A river (for example, the broad majestic Shannon)."""
    Role = Schema(schema_storage["Role"])
    """Represents additional information about a relationship or property. For example a
    Role can be used to say that a 'member' role linking some SportsTeam to a player
    occurred during a particular time period. Or that a Person's 'actor' role in a Movie
    was for some particular characterName. Such properties can be attached to a Role
    entity, which is then associated with the main entities using ordinary properties
    like 'member' or 'actor'.<br/><br/>

    See also <a href="http://blog.schema.org/2014/06/introducing-role.html">blog post</a>.
    """
    RoofingContractor = Schema(schema_storage["RoofingContractor"])
    """A roofing contractor."""
    Room = Schema(schema_storage["Room"])
    """A room is a distinguishable space within a structure, usually separated from
    other spaces by interior walls.

    (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Room">http://en.wikipedia.org/wiki/Room</a>).
    <br /><br />
    See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    RsvpAction = Schema(schema_storage["RsvpAction"])
    """The act of notifying an event organizer as to whether you expect to attend the
    event."""
    RsvpResponseMaybe = Schema(schema_storage["RsvpResponseMaybe"])
    """The invitee may or may not attend."""
    RsvpResponseNo = Schema(schema_storage["RsvpResponseNo"])
    """The invitee will not attend."""
    RsvpResponseType = Schema(schema_storage["RsvpResponseType"])
    """RsvpResponseType is an enumeration type whose instances represent responding to
    an RSVP request."""
    RsvpResponseYes = Schema(schema_storage["RsvpResponseYes"])
    """The invitee will attend."""
    SRP = Schema(schema_storage["SRP"])
    """Represents the suggested retail price ("SRP") of an offered product."""
    SafetyHealthAspect = Schema(schema_storage["SafetyHealthAspect"])
    """Content about the safety-related aspects of a health topic."""
    SaleEvent = Schema(schema_storage["SaleEvent"])
    """Event type: Sales event."""
    SalePrice = Schema(schema_storage["SalePrice"])
    """Represents a sale price (usually active for a limited period) of an offered
    product."""
    SatireOrParodyContent = Schema(schema_storage["SatireOrParodyContent"])
    """Content coded 'satire or content' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'satire or
    parody content': A video that was created as political or humorous commentary and is
    presented in that context. (Reshares of satire/parody content that do not include
    relevant context are more likely to fall under the “missing context”
    rating.)<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be 'satire or
    parody content': An image that was created as political or humorous commentary and
    is presented in that context. (Reshares of satire/parody content that do not include
    relevant context are more likely to fall under the “missing context”
    rating.)<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'satire or parody content': An image that was created as political or
    humorous commentary and is presented in that context. (Reshares of satire/parody
    content that do not include relevant context are more likely to fall under the
    “missing context” rating.)<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be 'satire or
    parody content': Audio that was created as political or humorous commentary and is
    presented in that context. (Reshares of satire/parody content that do not include
    relevant context are more likely to fall under the “missing context” rating.)
    """
    SatiricalArticle = Schema(schema_storage["SatiricalArticle"])
    """An <a class="localLink" href="#sc.Article">Article</a> whose content is primarily <a href="https://en.wikipedia.org/wiki/Satire">[satirical]</a> in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a <a class="localLink" href="#sc.NewsArticle">NewsArticle</a>. <a class="localLink" href="#sc.ScholarlyArticle">ScholarlyArticle</a>s are also sometimes satirized."""
    Saturday = Schema(schema_storage["Saturday"])
    """The day of the week between Friday and Sunday."""
    Schedule = Schema(schema_storage["Schedule"])
    """A schedule defines a repeating time period used to describe a regularly occurring
    <a class="localLink" href="#sc.Event">Event</a>.

    At a minimum a schedule will specify <a class="localLink"
    href="#sc.repeatFrequency">repeatFrequency</a> which describes the interval between
    occurences of the event. Additional information can be provided to specify the
    schedule more precisely. This includes identifying the day(s) of the week or month
    when the recurring event will take place, in addition to its start and end time.
    Schedules may also have start and end dates to indicate when they are active, e.g.
    to define a limited calendar of events.
    """
    ScheduleAction = Schema(schema_storage["ScheduleAction"])
    """Scheduling future actions, events, or tasks.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ReserveAction">ReserveAction</a>: Unlike
    ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc)
    towards a time slot / spatial allocation.</li> </ul>
    """
    ScholarlyArticle = Schema(schema_storage["ScholarlyArticle"])
    """A scholarly article."""
    School = Schema(schema_storage["School"])
    """A school."""
    SchoolDistrict = Schema(schema_storage["SchoolDistrict"])
    """A School District is an administrative area for the administration of schools."""
    ScreeningEvent = Schema(schema_storage["ScreeningEvent"])
    """A screening of a movie or other video."""
    ScreeningHealthAspect = Schema(schema_storage["ScreeningHealthAspect"])
    """Content about how to screen or further filter a topic."""
    Sculpture = Schema(schema_storage["Sculpture"])
    """A piece of sculpture."""
    SeaBodyOfWater = Schema(schema_storage["SeaBodyOfWater"])
    """A sea (for example, the Caspian sea)."""
    SearchAction = Schema(schema_storage["SearchAction"])
    """The act of searching for an object.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.FindAction">FindAction</a>: SearchAction
    generally leads to a FindAction, but not necessarily.</li> </ul>
    """
    SearchResultsPage = Schema(schema_storage["SearchResultsPage"])
    """Web page type: Search results page."""
    Season = Schema(schema_storage["Season"])
    """A media season e.g. tv, radio, video game etc."""
    Seat = Schema(schema_storage["Seat"])
    """Used to describe a seat, such as a reserved seat in an event reservation."""
    SeatingMap = Schema(schema_storage["SeatingMap"])
    """A seating map."""
    SeeDoctorHealthAspect = Schema(schema_storage["SeeDoctorHealthAspect"])
    """Information about questions that may be asked, when to see a professional,
    measures before seeing a doctor or content about the first consultation."""
    SeekToAction = Schema(schema_storage["SeekToAction"])
    """This is the <a class="localLink" href="#sc.Action">Action</a> of navigating to a
    specific <a class="localLink" href="#sc.startOffset">startOffset</a> timestamp
    within a <a class="localLink" href="#sc.VideoObject">VideoObject</a>, typically
    represented with a URL template structure."""
    SelfCareHealthAspect = Schema(schema_storage["SelfCareHealthAspect"])
    """Self care actions or measures that can be taken to sooth, health or avoid a
    topic.

    This may be carried at home and can be carried/managed by the person itself.
    """
    SelfStorage = Schema(schema_storage["SelfStorage"])
    """A self-storage facility."""
    SellAction = Schema(schema_storage["SellAction"])
    """The act of taking money from a buyer in exchange for goods or services rendered.

    An agent sells an object, product, or service to a buyer for a price. Reciprocal of
    BuyAction.
    """
    SendAction = Schema(schema_storage["SendAction"])
    """The act of physically/electronically dispatching an object for transfer from an
    origin to a destination.Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.ReceiveAction">ReceiveAction</a>: The
    reciprocal of SendAction.</li> <li><a class="localLink"
    href="#sc.GiveAction">GiveAction</a>: Unlike GiveAction, SendAction does not imply
    the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily
    giving it to you).</li> </ul>
    """
    Series = Schema(schema_storage["Series"])
    """A Series in schema.org is a group of related items, typically but not necessarily
    of the same kind.

    See also <a class="localLink" href="#sc.CreativeWorkSeries">CreativeWorkSeries</a>, <a class="localLink" href="#sc.EventSeries">EventSeries</a>.
    """
    Service = Schema(schema_storage["Service"])
    """A service provided by an organization, e.g. delivery service, print services,
    etc."""
    ServiceChannel = Schema(schema_storage["ServiceChannel"])
    """A means for accessing a service, e.g. a government office location, web site, or
    phone number."""
    ShareAction = Schema(schema_storage["ShareAction"])
    """The act of distributing content to people for their amusement or edification."""
    SheetMusic = Schema(schema_storage["SheetMusic"])
    """Printed music, as opposed to performed or recorded music."""
    ShippingDeliveryTime = Schema(schema_storage["ShippingDeliveryTime"])
    """ShippingDeliveryTime provides various pieces of information about delivery times
    for shipping."""
    ShippingRateSettings = Schema(schema_storage["ShippingRateSettings"])
    """A ShippingRateSettings represents re-usable pieces of shipping information.

    It is designed for publication on an URL that may be referenced via the <a class="localLink" href="#sc.shippingSettingsLink">shippingSettingsLink</a> property of an <a class="localLink" href="#sc.OfferShippingDetails">OfferShippingDetails</a>. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for <a class="localLink" href="#sc.shippingLabel">shippingLabel</a>.
    """
    ShoeStore = Schema(schema_storage["ShoeStore"])
    """A shoe store."""
    ShoppingCenter = Schema(schema_storage["ShoppingCenter"])
    """A shopping center or mall."""
    ShortStory = Schema(schema_storage["ShortStory"])
    """Short story or tale.

    A brief work of literature, usually written in narrative prose.
    """
    SideEffectsHealthAspect = Schema(schema_storage["SideEffectsHealthAspect"])
    """Side effects that can be observed from the usage of the topic."""
    SingleBlindedTrial = Schema(schema_storage["SingleBlindedTrial"])
    """A trial design in which the researcher knows which treatment the patient was
    randomly assigned to but the patient does not."""
    SingleCenterTrial = Schema(schema_storage["SingleCenterTrial"])
    """A trial that takes place at a single center."""
    SingleFamilyResidence = Schema(schema_storage["SingleFamilyResidence"])
    """Residence type: Single-family home."""
    SinglePlayer = Schema(schema_storage["SinglePlayer"])
    """Play mode: SinglePlayer. Which is played by a lone player."""
    SingleRelease = Schema(schema_storage["SingleRelease"])
    """SingleRelease."""
    SiteNavigationElement = Schema(schema_storage["SiteNavigationElement"])
    """A navigation element of the page."""
    SizeGroupEnumeration = Schema(schema_storage["SizeGroupEnumeration"])
    """Enumerates common size groups for various product categories."""
    SizeSpecification = Schema(schema_storage["SizeSpecification"])
    """Size related properties of a product, typically a size code (<a class="localLink"
    href="#sc.name">name</a>) and optionally a <a class="localLink"
    href="#sc.sizeSystem">sizeSystem</a>, <a class="localLink"
    href="#sc.sizeGroup">sizeGroup</a>, and product measurements (<a class="localLink"
    href="#sc.hasMeasurement">hasMeasurement</a>).

    In addition, the intended audience can be defined through <a class="localLink" href="#sc.suggestedAge">suggestedAge</a>, <a class="localLink" href="#sc.suggestedGender">suggestedGender</a>, and suggested body measurements (<a class="localLink" href="#sc.suggestedMeasurement">suggestedMeasurement</a>).
    """
    SizeSystemEnumeration = Schema(schema_storage["SizeSystemEnumeration"])
    """Enumerates common size systems for different categories of products, for example
    "EN-13402" or "UK" for wearables or "Imperial" for screws."""
    SizeSystemImperial = Schema(schema_storage["SizeSystemImperial"])
    """Imperial size system."""
    SizeSystemMetric = Schema(schema_storage["SizeSystemMetric"])
    """Metric size system."""
    SkiResort = Schema(schema_storage["SkiResort"])
    """A ski resort."""
    Skin = Schema(schema_storage["Skin"])
    """Skin assessment with clinical examination."""
    SocialEvent = Schema(schema_storage["SocialEvent"])
    """Event type: Social event."""
    SocialMediaPosting = Schema(schema_storage["SocialMediaPosting"])
    """A post to a social media platform, including blog posts, tweets, Facebook posts,
    etc."""
    SoftwareApplication = Schema(schema_storage["SoftwareApplication"])
    """A software application."""
    SoftwareSourceCode = Schema(schema_storage["SoftwareSourceCode"])
    """Computer programming source code.

    Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    SoldOut = Schema(schema_storage["SoldOut"])
    """Indicates that the item has sold out."""
    SolveMathAction = Schema(schema_storage["SolveMathAction"])
    """The action that takes in a math expression and directs users to a page
    potentially capable of solving/simplifying that expression."""
    SomeProducts = Schema(schema_storage["SomeProducts"])
    """A placeholder for multiple similar products of the same kind."""
    SoundtrackAlbum = Schema(schema_storage["SoundtrackAlbum"])
    """SoundtrackAlbum."""
    SpeakableSpecification = Schema(schema_storage["SpeakableSpecification"])
    """A SpeakableSpecification indicates (typically via <a class="localLink"
    href="#sc.xpath">xpath</a> or <a class="localLink"
    href="#sc.cssSelector">cssSelector</a>) sections of a document that are highlighted
    as particularly <a class="localLink" href="#sc.speakable">speakable</a>.

    Instances of this type are expected to be used primarily as values of the <a
    class="localLink" href="#sc.speakable">speakable</a> property.
    """
    SpecialAnnouncement = Schema(schema_storage["SpecialAnnouncement"])
    """A SpecialAnnouncement combines a simple date-stamped textual information update
    with contextualized Web links and other structured data.  It represents an
    information update made by a locally-oriented organization, for example schools,
    pharmacies, healthcare providers,  community groups, police, local
    government.<br/><br/>

    For work in progress guidelines on Coronavirus-related markup see <a href="https://docs.google.com/document/d/14ikaGCKxo50rRM7nvKSlbUpjyIk2WMQd3IkB1lItlrM/edit#">this doc</a>.<br/><br/>

    The motivating scenario for SpecialAnnouncement is the <a href="https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic">Coronavirus pandemic</a>, and the initial vocabulary is oriented to this urgent situation. Schema.org
    expect to improve the markup iteratively as it is deployed and as feedback emerges from use. In addition to our
    usual <a href="https://github.com/schemaorg/schemaorg/issues/2490">Github entry</a>, feedback comments can also be provided in <a href="https://docs.google.com/document/d/1fpdFFxk8s87CWwACs53SGkYv3aafSxz_DTtOQxMrBJQ/edit#">this document</a>.<br/><br/>

    While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like <a href="https://en.wikipedia.org/wiki/Common_Alerting_Protocol">CAP</a>, although there may be overlaps. The intent is to cover
    the kinds of everyday practical information being posted to existing websites during an emergency situation.<br/><br/>

    Several kinds of information can be provided:<br/><br/>

    We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and
    "url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known
    URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20_coronavirus_pandemic" or "https://www.wikidata.org/wiki/Q81068910".<br/><br/>

    For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property's value. For an inline description, use a <a class="localLink" href="#sc.WebContent">WebContent</a> type, and provide the url as a property of that, alongside at least a simple "<a class="localLink" href="#sc.text">text</a>" summary of the page. It is
    unlikely that a single SpecialAnnouncement will need all of the possible properties simultaneously.<br/><br/>

    We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info, <a class="localLink" href="#sc.openingHours">openingHours</a>, <a class="localLink" href="#sc.Event">Event</a>, <a class="localLink" href="#sc.FAQPage">FAQPage</a> etc. By linking to those pages from a <a class="localLink" href="#sc.SpecialAnnouncement">SpecialAnnouncement</a> you can help make it clearer that the events are related to the situation (e.g. Coronavirus) indicated by the <a class="localLink" href="#sc.category">category</a> property of the <a class="localLink" href="#sc.SpecialAnnouncement">SpecialAnnouncement</a>.<br/><br/>

    Many <a class="localLink" href="#sc.SpecialAnnouncement">SpecialAnnouncement</a>s will relate to particular regions and to identifiable local organizations. Use <a class="localLink" href="#sc.spatialCoverage">spatialCoverage</a> for the region, and <a class="localLink" href="#sc.announcementLocation">announcementLocation</a> to indicate specific <a class="localLink" href="#sc.LocalBusiness">LocalBusiness</a>es and <a class="localLink" href="#sc.CivicStructure">CivicStructure</a>s. If the announcement affects both a particular region and a specific location (for example, a library closure that serves an entire region), use both <a class="localLink" href="#sc.spatialCoverage">spatialCoverage</a> and <a class="localLink" href="#sc.announcementLocation">announcementLocation</a>.<br/><br/>

    The <a class="localLink" href="#sc.about">about</a> property can be used to indicate entities that are the focus of the announcement. We now recommend using <a class="localLink" href="#sc.about">about</a> only
    for representing non-location entities (e.g. a <a class="localLink" href="#sc.Course">Course</a> or a <a class="localLink" href="#sc.RadioStation">RadioStation</a>). For places, use <a class="localLink" href="#sc.announcementLocation">announcementLocation</a> and <a class="localLink" href="#sc.spatialCoverage">spatialCoverage</a>. Consumers of this markup should be aware that the initial design encouraged the use of /about for locations too.<br/><br/>

    The basic content of <a class="localLink" href="#sc.SpecialAnnouncement">SpecialAnnouncement</a> is similar to that of an <a href="https://en.wikipedia.org/wiki/RSS">RSS</a> or <a href="https://en.wikipedia.org/wiki/Atom_(Web_standard)">Atom</a> feed. For publishers without such feeds, basic feed-like information can be shared by posting
    <a class="localLink" href="#sc.SpecialAnnouncement">SpecialAnnouncement</a> updates in a page, e.g. using JSON-LD. For sites with Atom/RSS functionality, you can point to a feed
    with the <a class="localLink" href="#sc.webFeed">webFeed</a> property. This can be a simple URL, or an inline <a class="localLink" href="#sc.DataFeed">DataFeed</a> object, with <a class="localLink" href="#sc.encodingFormat">encodingFormat</a> providing
    media type information e.g. "application/rss+xml" or "application/atom+xml".
    """
    Specialty = Schema(schema_storage["Specialty"])
    """Any branch of a field in which people typically develop specific expertise,
    usually after significant study, time, and effort."""
    SpeechPathology = Schema(schema_storage["SpeechPathology"])
    """The scientific study and treatment of defects, disorders, and malfunctions of
    speech and voice, as stuttering, lisping, or lalling, and of language disturbances,
    as aphasia or delayed language acquisition."""
    SpokenWordAlbum = Schema(schema_storage["SpokenWordAlbum"])
    """SpokenWordAlbum."""
    SportingGoodsStore = Schema(schema_storage["SportingGoodsStore"])
    """A sporting goods store."""
    SportsActivityLocation = Schema(schema_storage["SportsActivityLocation"])
    """A sports location, such as a playing field."""
    SportsClub = Schema(schema_storage["SportsClub"])
    """A sports club."""
    SportsEvent = Schema(schema_storage["SportsEvent"])
    """Event type: Sports event."""
    SportsOrganization = Schema(schema_storage["SportsOrganization"])
    """Represents the collection of all sports organizations, including sports teams,
    governing bodies, and sports associations."""
    SportsTeam = Schema(schema_storage["SportsTeam"])
    """Organization: Sports team."""
    SpreadsheetDigitalDocument = Schema(schema_storage["SpreadsheetDigitalDocument"])
    """A spreadsheet file."""
    StadiumOrArena = Schema(schema_storage["StadiumOrArena"])
    """A stadium."""
    StagedContent = Schema(schema_storage["StagedContent"])
    """Content coded 'staged content' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'staged
    content': A video that has been created using actors or similarly
    contrived.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be 'staged
    content': An image that was created using actors or similarly contrived, such as a
    screenshot of a fake tweet.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'staged content': An image that was created using actors or similarly
    contrived, such as a screenshot of a fake tweet.<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be 'staged
    content': Audio that has been created using actors or similarly contrived.
    """
    StagesHealthAspect = Schema(schema_storage["StagesHealthAspect"])
    """Stages that can be observed from a topic."""
    State = Schema(schema_storage["State"])
    """A state or province of a country."""
    StatisticalPopulation = Schema(schema_storage["StatisticalPopulation"])
    """A StatisticalPopulation is a set of instances of a certain given type that
    satisfy some set of constraints.

    The property <a class="localLink" href="#sc.populationType">populationType</a> is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a <a class="localLink" href="#sc.StatisticalPopulation">StatisticalPopulation</a> representing all <a class="localLink" href="#sc.Person">Person</a>s with a <a class="localLink" href="#sc.homeLocation">homeLocation</a> of East Podunk California, would be described by applying the appropriate <a class="localLink" href="#sc.homeLocation">homeLocation</a> and <a class="localLink" href="#sc.populationType">populationType</a> properties to a <a class="localLink" href="#sc.StatisticalPopulation">StatisticalPopulation</a> item that stands for that set of people.
    The properties <a class="localLink" href="#sc.numConstraints">numConstraints</a> and <a class="localLink" href="#sc.constrainingProperty">constrainingProperty</a> are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statistical
    population, and does not imply that the population consists of people. For example, a <a class="localLink" href="#sc.populationType">populationType</a> of <a class="localLink" href="#sc.Event">Event</a> or <a class="localLink" href="#sc.NewsArticle">NewsArticle</a> could be used. See also <a class="localLink" href="#sc.Observation">Observation</a>, and the <a href="/docs/data-and-datasets.html">data and datasets</a> overview for more details.
    """
    StatusEnumeration = Schema(schema_storage["StatusEnumeration"])
    """Lists or enumerations dealing with status types."""
    SteeringPositionValue = Schema(schema_storage["SteeringPositionValue"])
    """A value indicating a steering position."""
    Store = Schema(schema_storage["Store"])
    """A retail good store."""
    StoreCreditRefund = Schema(schema_storage["StoreCreditRefund"])
    """A StoreCreditRefund ..."""
    StrengthTraining = Schema(schema_storage["StrengthTraining"])
    """Physical activity that is engaged in to improve muscle and bone strength.

    Also referred to as resistance training.
    """
    StructuredValue = Schema(schema_storage["StructuredValue"])
    """Structured values are used when the value of a property has a more complex
    structure than simply being a textual value or a reference to another thing."""
    StudioAlbum = Schema(schema_storage["StudioAlbum"])
    """StudioAlbum."""
    StupidType = Schema(schema_storage["StupidType"])
    """A StupidType for testing."""
    SubscribeAction = Schema(schema_storage["SubscribeAction"])
    """The act of forming a personal connection with someone/something (object)
    unidirectionally/asymmetrically to get updates pushed to.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.FollowAction">FollowAction</a>: Unlike
    FollowAction, SubscribeAction implies that the subscriber acts as a passive agent
    being constantly/actively pushed for updates.</li> <li><a class="localLink"
    href="#sc.RegisterAction">RegisterAction</a>: Unlike RegisterAction, SubscribeAction
    implies that the agent is interested in continuing receiving updates from the
    object.</li> <li><a class="localLink" href="#sc.JoinAction">JoinAction</a>: Unlike
    JoinAction, SubscribeAction implies that the agent is interested in continuing
    receiving updates from the object.</li> </ul>
    """
    Subscription = Schema(schema_storage["Subscription"])
    """Represents the subscription pricing component of the total price for an offered
    product."""
    Substance = Schema(schema_storage["Substance"])
    """Any matter of defined composition that has discrete existence, whose origin may
    be biological, mineral or chemical."""
    SubwayStation = Schema(schema_storage["SubwayStation"])
    """A subway station."""
    Suite = Schema(schema_storage["Suite"])
    """A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (Source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>."""
    Sunday = Schema(schema_storage["Sunday"])
    """The day of the week between Saturday and Monday."""
    SuperficialAnatomy = Schema(schema_storage["SuperficialAnatomy"])
    """Anatomical features that can be observed by sight (without dissection), including
    the form and proportions of the human body as well as surface landmarks that
    correspond to deeper subcutaneous structures.

    Superficial anatomy plays an important role in sports medicine, phlebotomy, and
    other medical specialties as underlying anatomical structures can be identified
    through surface palpation. For example, during back surgery, superficial anatomy can
    be used to palpate and count vertebrae to find the site of incision. Or in
    phlebotomy, superficial anatomy can be used to locate an underlying vein; for
    example, the median cubital vein can be located by palpating the borders of the
    cubital fossa (such as the epicondyles of the humerus) and then looking for the
    superficial signs of the vein, such as size, prominence, ability to refill after
    depression, and feel of surrounding tissue support. As another example, in a
    subluxation (dislocation) of the glenohumeral joint, the bony structure becomes
    pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing
    the edges of the scapula to be superficially visible. Here, the superficial anatomy
    is the visible edges of the scapula, implying the underlying dislocation of the
    joint (the related anatomical structure).
    """
    Surgical = Schema(schema_storage["Surgical"])
    """A specific branch of medical science that pertains to treating diseases, injuries
    and deformities by manual and instrumental means."""
    SurgicalProcedure = Schema(schema_storage["SurgicalProcedure"])
    """A medical procedure involving an incision with instruments; performed for
    diagnose, or therapeutic purposes."""
    SuspendAction = Schema(schema_storage["SuspendAction"])
    """The act of momentarily pausing a device or application (e.g. pause music playback
    or pause a timer)."""
    Suspended = Schema(schema_storage["Suspended"])
    """Suspended."""
    SymptomsHealthAspect = Schema(schema_storage["SymptomsHealthAspect"])
    """Symptoms or related symptoms of a Topic."""
    Synagogue = Schema(schema_storage["Synagogue"])
    """A synagogue."""
    TVClip = Schema(schema_storage["TVClip"])
    """A short TV program or a segment/part of a TV program."""
    TVEpisode = Schema(schema_storage["TVEpisode"])
    """A TV episode which can be part of a series or season."""
    TVSeason = Schema(schema_storage["TVSeason"])
    """Season dedicated to TV broadcast and associated online delivery."""
    TVSeries = Schema(schema_storage["TVSeries"])
    """CreativeWorkSeries dedicated to TV broadcast and associated online delivery."""
    Table = Schema(schema_storage["Table"])
    """A table on a Web page."""
    TakeAction = Schema(schema_storage["TakeAction"])
    """The act of gaining ownership of an object from an origin. Reciprocal of
    GiveAction.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.GiveAction">GiveAction</a>: The reciprocal
    of TakeAction.</li> <li><a class="localLink"
    href="#sc.ReceiveAction">ReceiveAction</a>: Unlike ReceiveAction, TakeAction implies
    that ownership has been transfered.</li> </ul>
    """
    TattooParlor = Schema(schema_storage["TattooParlor"])
    """A tattoo parlor."""
    Taxi = Schema(schema_storage["Taxi"])
    """A taxi."""
    TaxiReservation = Schema(schema_storage["TaxiReservation"])
    """A reservation for a taxi.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    TaxiService = Schema(schema_storage["TaxiService"])
    """A service for a vehicle for hire with a driver for local travel.

    Fares are usually calculated based on distance traveled.
    """
    TaxiStand = Schema(schema_storage["TaxiStand"])
    """A taxi stand."""
    TaxiVehicleUsage = Schema(schema_storage["TaxiVehicleUsage"])
    """Indicates the usage of the car as a taxi."""
    TechArticle = Schema(schema_storage["TechArticle"])
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc."""
    TelevisionChannel = Schema(schema_storage["TelevisionChannel"])
    """A unique instance of a television BroadcastService on a CableOrSatelliteService
    lineup."""
    TelevisionStation = Schema(schema_storage["TelevisionStation"])
    """A television station."""
    TennisComplex = Schema(schema_storage["TennisComplex"])
    """A tennis complex."""
    Terminated = Schema(schema_storage["Terminated"])
    """Terminated."""
    Text = Schema(schema_storage["Text"])
    """Data type: Text."""
    TextDigitalDocument = Schema(schema_storage["TextDigitalDocument"])
    """A file composed primarily of text."""
    TheaterEvent = Schema(schema_storage["TheaterEvent"])
    """Event type: Theater performance."""
    TheaterGroup = Schema(schema_storage["TheaterGroup"])
    """A theater group or company, for example, the Royal Shakespeare Company or Druid
    Theatre."""
    Therapeutic = Schema(schema_storage["Therapeutic"])
    """A medical device used for therapeutic purposes."""
    TherapeuticProcedure = Schema(schema_storage["TherapeuticProcedure"])
    """A medical procedure intended primarily for therapeutic purposes, aimed at
    improving a health condition."""
    Thesis = Schema(schema_storage["Thesis"])
    """A thesis or dissertation document submitted in support of candidature for an
    academic degree or professional qualification."""
    Thing = Schema(schema_storage["Thing"])
    """The most generic type of item."""
    Throat = Schema(schema_storage["Throat"])
    """Throat assessment with  clinical examination."""
    Thursday = Schema(schema_storage["Thursday"])
    """The day of the week between Wednesday and Friday."""
    Ticket = Schema(schema_storage["Ticket"])
    """Used to describe a ticket to an event, a flight, a bus ride, etc."""
    TieAction = Schema(schema_storage["TieAction"])
    """The act of reaching a draw in a competitive activity."""
    Time = Schema(schema_storage["Time"])
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see <a href="http://www.w3.org/TR/xmlschema-2/#time">XML schema for details</a>)."""
    TipAction = Schema(schema_storage["TipAction"])
    """The act of giving money voluntarily to a beneficiary in recognition of services
    rendered."""
    TireShop = Schema(schema_storage["TireShop"])
    """A tire shop."""
    TollFree = Schema(schema_storage["TollFree"])
    """The associated telephone number is toll free."""
    TouristAttraction = Schema(schema_storage["TouristAttraction"])
    """A tourist attraction.

    In principle any Thing can be a <a class="localLink" href="#sc.TouristAttraction">TouristAttraction</a>, from a <a class="localLink" href="#sc.Mountain">Mountain</a> and <a class="localLink" href="#sc.LandmarksOrHistoricalBuildings">LandmarksOrHistoricalBuildings</a> to a <a class="localLink" href="#sc.LocalBusiness">LocalBusiness</a>.  This Type can be used on its own to describe a general <a class="localLink" href="#sc.TouristAttraction">TouristAttraction</a>, or be used as an <a class="localLink" href="#sc.additionalType">additionalType</a> to add tourist attraction properties to any other type.  (See examples below)
    """
    TouristDestination = Schema(schema_storage["TouristDestination"])
    """A tourist destination.

    In principle any <a class="localLink" href="#sc.Place">Place</a> can be a <a class="localLink" href="#sc.TouristDestination">TouristDestination</a> from a <a class="localLink" href="#sc.City">City</a>, Region or <a class="localLink" href="#sc.Country">Country</a> to an <a class="localLink" href="#sc.AmusementPark">AmusementPark</a> or <a class="localLink" href="#sc.Hotel">Hotel</a>. This Type can be used on its own to describe a general <a class="localLink" href="#sc.TouristDestination">TouristDestination</a>, or be used as an <a class="localLink" href="#sc.additionalType">additionalType</a> to add tourist relevant properties to any other <a class="localLink" href="#sc.Place">Place</a>.  A <a class="localLink" href="#sc.TouristDestination">TouristDestination</a> is defined as a <a class="localLink" href="#sc.Place">Place</a> that contains, or is colocated with, one or more <a class="localLink" href="#sc.TouristAttraction">TouristAttraction</a>s, often linked by a similar theme or interest to a particular <a class="localLink" href="#sc.touristType">touristType</a>. The <a href="http://www2.unwto.org/">UNWTO</a> defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.
    (See examples below).
    """
    TouristInformationCenter = Schema(schema_storage["TouristInformationCenter"])
    """A tourist information center."""
    TouristTrip = Schema(schema_storage["TouristTrip"])
    """A tourist trip.

    A created itinerary of visits to one or more places of interest (<a class="localLink" href="#sc.TouristAttraction">TouristAttraction</a>/<a class="localLink" href="#sc.TouristDestination">TouristDestination</a>) often linked by a similar theme, geographic area, or interest to a particular <a class="localLink" href="#sc.touristType">touristType</a>. The <a href="http://www2.unwto.org/">UNWTO</a> defines tourism trip as the Trip taken by visitors.
    (See examples below).
    """
    Toxicologic = Schema(schema_storage["Toxicologic"])
    """A specific branch of medical science that is concerned with poisons, their
    nature, effects and detection and involved in the treatment of poisoning."""
    ToyStore = Schema(schema_storage["ToyStore"])
    """A toy store."""
    TrackAction = Schema(schema_storage["TrackAction"])
    """An agent tracks an object for updates.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.FollowAction">FollowAction</a>: Unlike
    FollowAction, TrackAction refers to the interest on the location of innanimates
    objects.</li> <li><a class="localLink"
    href="#sc.SubscribeAction">SubscribeAction</a>: Unlike SubscribeAction, TrackAction
    refers to  the interest on the location of innanimate objects.</li> </ul>
    """
    TradeAction = Schema(schema_storage["TradeAction"])
    """The act of participating in an exchange of goods and services for monetary
    compensation.

    An agent trades an object, product or service with a participant in exchange for a
    one time or periodic payment.
    """
    TraditionalChinese = Schema(schema_storage["TraditionalChinese"])
    """A system of medicine based on common theoretical concepts that originated in
    China and evolved over thousands of years, that uses herbs, acupuncture, exercise,
    massage, dietary therapy, and other methods to treat a wide range of conditions."""
    TrainReservation = Schema(schema_storage["TrainReservation"])
    """A reservation for train travel.<br/><br/>

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use <a class="localLink" href="#sc.Offer">Offer</a>.
    """
    TrainStation = Schema(schema_storage["TrainStation"])
    """A train station."""
    TrainTrip = Schema(schema_storage["TrainTrip"])
    """A trip on a commercial train line."""
    TransferAction = Schema(schema_storage["TransferAction"])
    """The act of transferring/moving (abstract or concrete) animate or inanimate
    objects from one place to another."""
    TransformedContent = Schema(schema_storage["TransformedContent"])
    """Content coded 'transformed content' in a <a class="localLink"
    href="#sc.MediaReview">MediaReview</a>, considered in the context of how it was
    published or shared.<br/><br/>

    For a <a class="localLink" href="#sc.VideoObject">VideoObject</a> to be 'transformed
    content':  or all of the video has been manipulated to transform the footage itself.
    This category includes using tools like the Adobe Suite to change the speed of the
    video, add or remove visual elements or dub audio. Deepfakes are also a subset of
    transformation.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> to be transformed
    content': Adding or deleting visual elements to give the image a different meaning
    with the intention to mislead.<br/><br/>

    For an <a class="localLink" href="#sc.ImageObject">ImageObject</a> with embedded
    text to be 'transformed content': Adding or deleting visual elements to give the
    image a different meaning with the intention to mislead.<br/><br/>

    For an <a class="localLink" href="#sc.AudioObject">AudioObject</a> to be
    'transformed content': Part or all of the audio has been manipulated to alter the
    words or sounds, or the audio has been synthetically generated, such as to create a
    sound-alike voice.
    """
    TransitMap = Schema(schema_storage["TransitMap"])
    """A transit map."""
    TravelAction = Schema(schema_storage["TravelAction"])
    """The act of traveling from an fromLocation to a destination by a specified mode of
    transport, optionally with participants."""
    TravelAgency = Schema(schema_storage["TravelAgency"])
    """A travel agency."""
    TreatmentIndication = Schema(schema_storage["TreatmentIndication"])
    """An indication for treating an underlying condition, symptom, etc."""
    TreatmentsHealthAspect = Schema(schema_storage["TreatmentsHealthAspect"])
    """Treatments or related therapies for a Topic."""
    Trip = Schema(schema_storage["Trip"])
    """A trip or journey.

    An itinerary of visits to one or more places.
    """
    TripleBlindedTrial = Schema(schema_storage["TripleBlindedTrial"])
    """A trial design in which neither the researcher, the person administering the
    therapy nor the patient knows the details of the treatment the patient was randomly
    assigned to."""
    _True = Schema(schema_storage["True"])
    """@public The boolean value true."""
    Tuesday = Schema(schema_storage["Tuesday"])
    """The day of the week between Monday and Wednesday."""
    TypeAndQuantityNode = Schema(schema_storage["TypeAndQuantityNode"])
    """A structured value indicating the quantity, unit of measurement, and business
    function of goods included in a bundle offer."""
    TypesHealthAspect = Schema(schema_storage["TypesHealthAspect"])
    """Categorization and other types related to a topic."""
    UKNonprofitType = Schema(schema_storage["UKNonprofitType"])
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom."""
    UKTrust = Schema(schema_storage["UKTrust"])
    """UKTrust: Non-profit type referring to a UK trust."""
    URL = Schema(schema_storage["URL"])
    """Data type: URL."""
    USNonprofitType = Schema(schema_storage["USNonprofitType"])
    """USNonprofitType: Non-profit organization type originating from the United States."""
    Ultrasound = Schema(schema_storage["Ultrasound"])
    """Ultrasound imaging."""
    UnRegisterAction = Schema(schema_storage["UnRegisterAction"])
    """The act of un-registering from a service.<br/><br/>

    Related actions:<br/><br/>

    <ul> <li><a class="localLink" href="#sc.RegisterAction">RegisterAction</a>: antonym
    of UnRegisterAction.</li> <li><a class="localLink"
    href="#sc.LeaveAction">LeaveAction</a>: Unlike LeaveAction, UnRegisterAction implies
    that you are unregistering from a service you werer previously registered, rather
    than leaving a team/group of people.</li> </ul>
    """
    UnemploymentSupport = Schema(schema_storage["UnemploymentSupport"])
    """UnemploymentSupport: this is a benefit for unemployment support."""
    UnincorporatedAssociationCharity = Schema(
        schema_storage["UnincorporatedAssociationCharity"]
    )
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK)."""
    UnitPriceSpecification = Schema(schema_storage["UnitPriceSpecification"])
    """The price asked for a given offer by the respective organization or person."""
    UnofficialLegalValue = Schema(schema_storage["UnofficialLegalValue"])
    """Indicates that a document has no particular or special standing (e.g. a
    republication of a law by a private publisher)."""
    UpdateAction = Schema(schema_storage["UpdateAction"])
    """The act of managing by changing/editing the state of the object."""
    Urologic = Schema(schema_storage["Urologic"])
    """A specific branch of medical science that is concerned with the diagnosis and
    treatment of diseases pertaining to the urinary tract and the urogenital system."""
    UsageOrScheduleHealthAspect = Schema(schema_storage["UsageOrScheduleHealthAspect"])
    """Content about how, when, frequency and dosage of a topic."""
    UseAction = Schema(schema_storage["UseAction"])
    """The act of applying an object to its intended purpose."""
    UsedCondition = Schema(schema_storage["UsedCondition"])
    """Indicates that the item is used."""
    UserBlocks = Schema(schema_storage["UserBlocks"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserCheckins = Schema(schema_storage["UserCheckins"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserComments = Schema(schema_storage["UserComments"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserDownloads = Schema(schema_storage["UserDownloads"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserInteraction = Schema(schema_storage["UserInteraction"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserLikes = Schema(schema_storage["UserLikes"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserPageVisits = Schema(schema_storage["UserPageVisits"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserPlays = Schema(schema_storage["UserPlays"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserPlusOnes = Schema(schema_storage["UserPlusOnes"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    UserReview = Schema(schema_storage["UserReview"])
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in
    contrast with <a class="localLink" href="#sc.CriticReview">CriticReview</a>."""
    UserTweets = Schema(schema_storage["UserTweets"])
    """UserInteraction and its subtypes is an old way of talking about users interacting
    with pages.

    It is generally better to use <a class="localLink"
    href="#sc.Action">Action</a>-based vocabulary, alongside types such as <a
    class="localLink" href="#sc.Comment">Comment</a>.
    """
    VeganDiet = Schema(schema_storage["VeganDiet"])
    """A diet exclusive of all animal products."""
    VegetarianDiet = Schema(schema_storage["VegetarianDiet"])
    """A diet exclusive of animal meat."""
    Vehicle = Schema(schema_storage["Vehicle"])
    """A vehicle is a device that is designed or used to transport people or cargo over
    land, water, air, or through space."""
    Vein = Schema(schema_storage["Vein"])
    """A type of blood vessel that specifically carries blood to the heart."""
    VenueMap = Schema(schema_storage["VenueMap"])
    """A venue map (e.g. for malls, auditoriums, museums, etc.)."""
    Vessel = Schema(schema_storage["Vessel"])
    """A component of the human body circulatory system comprised of an intricate
    network of hollow tubes that transport blood throughout the entire body."""
    VeterinaryCare = Schema(schema_storage["VeterinaryCare"])
    """A vet's office."""
    VideoGallery = Schema(schema_storage["VideoGallery"])
    """Web page type: Video gallery page."""
    VideoGame = Schema(schema_storage["VideoGame"])
    """A video game is an electronic game that involves human interaction with a user
    interface to generate visual feedback on a video device."""
    VideoGameClip = Schema(schema_storage["VideoGameClip"])
    """A short segment/part of a video game."""
    VideoGameSeries = Schema(schema_storage["VideoGameSeries"])
    """A video game series."""
    VideoObject = Schema(schema_storage["VideoObject"])
    """A video file."""
    ViewAction = Schema(schema_storage["ViewAction"])
    """The act of consuming static visual content."""
    VinylFormat = Schema(schema_storage["VinylFormat"])
    """VinylFormat."""
    VirtualLocation = Schema(schema_storage["VirtualLocation"])
    """An online or virtual location for attending events.

    For example, one may attend an online seminar or educational event. While a virtual
    location may be used as the location of an event, virtual locations should not be
    confused with physical locations in the real world.
    """
    Virus = Schema(schema_storage["Virus"])
    """Pathogenic virus that causes viral infection."""
    VisualArtsEvent = Schema(schema_storage["VisualArtsEvent"])
    """Event type: Visual arts event."""
    VisualArtwork = Schema(schema_storage["VisualArtwork"])
    """A work of art that is primarily visual in character."""
    VitalSign = Schema(schema_storage["VitalSign"])
    """Vital signs are measures of various physiological functions in order to assess
    the most basic body functions."""
    Volcano = Schema(schema_storage["Volcano"])
    """A volcano, like Fuji san."""
    VoteAction = Schema(schema_storage["VoteAction"])
    """The act of expressing a preference from a fixed/finite/structured set of
    choices/options."""
    WPAdBlock = Schema(schema_storage["WPAdBlock"])
    """An advertising section of the page."""
    WPFooter = Schema(schema_storage["WPFooter"])
    """The footer section of the page."""
    WPHeader = Schema(schema_storage["WPHeader"])
    """The header section of the page."""
    WPSideBar = Schema(schema_storage["WPSideBar"])
    """A sidebar section of the page."""
    WantAction = Schema(schema_storage["WantAction"])
    """The act of expressing a desire about the object.

    An agent wants an object.
    """
    WarrantyPromise = Schema(schema_storage["WarrantyPromise"])
    """A structured value representing the duration and scope of services that will be
    provided to a customer free of charge in case of a defect or malfunction of a
    product."""
    WarrantyScope = Schema(schema_storage["WarrantyScope"])
    """A range of of services that will be provided to a customer free of charge in case
    of a defect or malfunction of a product.<br/><br/>

    Commonly used values:<br/><br/>

    <ul>
    <li>http://purl.org/goodrelations/v1#Labor-BringIn</li>
    <li>http://purl.org/goodrelations/v1#PartsAndLabor-BringIn</li>
    <li>http://purl.org/goodrelations/v1#PartsAndLabor-PickUp</li>
    </ul>
    """
    WatchAction = Schema(schema_storage["WatchAction"])
    """The act of consuming dynamic/moving visual content."""
    Waterfall = Schema(schema_storage["Waterfall"])
    """A waterfall, like Niagara."""
    WearAction = Schema(schema_storage["WearAction"])
    """The act of dressing oneself in clothing."""
    WearableMeasurementBack = Schema(schema_storage["WearableMeasurementBack"])
    """Measurement of the back section, for example of a jacket."""
    WearableMeasurementChestOrBust = Schema(
        schema_storage["WearableMeasurementChestOrBust"]
    )
    """Measurement of the chest/bust section, for example of a suit."""
    WearableMeasurementCollar = Schema(schema_storage["WearableMeasurementCollar"])
    """Measurement of the collar, for example of a shirt."""
    WearableMeasurementCup = Schema(schema_storage["WearableMeasurementCup"])
    """Measurement of the cup, for example of a bra."""
    WearableMeasurementHeight = Schema(schema_storage["WearableMeasurementHeight"])
    """Measurement of the height, for example the heel height of a shoe."""
    WearableMeasurementHips = Schema(schema_storage["WearableMeasurementHips"])
    """Measurement of the hip section, for example of a skirt."""
    WearableMeasurementInseam = Schema(schema_storage["WearableMeasurementInseam"])
    """Measurement of the inseam, for example of pants."""
    WearableMeasurementLength = Schema(schema_storage["WearableMeasurementLength"])
    """Represents the length, for example of a dress."""
    WearableMeasurementOutsideLeg = Schema(
        schema_storage["WearableMeasurementOutsideLeg"]
    )
    """Measurement of the outside leg, for example of pants."""
    WearableMeasurementSleeve = Schema(schema_storage["WearableMeasurementSleeve"])
    """Measurement of the sleeve length, for example of a shirt."""
    WearableMeasurementTypeEnumeration = Schema(
        schema_storage["WearableMeasurementTypeEnumeration"]
    )
    """Enumerates common types of measurement for wearables products."""
    WearableMeasurementWaist = Schema(schema_storage["WearableMeasurementWaist"])
    """Measurement of the waist section, for example of pants."""
    WearableMeasurementWidth = Schema(schema_storage["WearableMeasurementWidth"])
    """Measurement of the width, for example of shoes."""
    WearableSizeGroupBig = Schema(schema_storage["WearableSizeGroupBig"])
    """Size group "Big" for wearables."""
    WearableSizeGroupBoys = Schema(schema_storage["WearableSizeGroupBoys"])
    """Size group "Boys" for wearables."""
    WearableSizeGroupEnumeration = Schema(
        schema_storage["WearableSizeGroupEnumeration"]
    )
    """Enumerates common size groups (also known as "size types") for wearable
    products."""
    WearableSizeGroupExtraShort = Schema(schema_storage["WearableSizeGroupExtraShort"])
    """Size group "Extra Short" for wearables."""
    WearableSizeGroupExtraTall = Schema(schema_storage["WearableSizeGroupExtraTall"])
    """Size group "Extra Tall" for wearables."""
    WearableSizeGroupGirls = Schema(schema_storage["WearableSizeGroupGirls"])
    """Size group "Girls" for wearables."""
    WearableSizeGroupHusky = Schema(schema_storage["WearableSizeGroupHusky"])
    """Size group "Husky" (or "Stocky") for wearables."""
    WearableSizeGroupInfants = Schema(schema_storage["WearableSizeGroupInfants"])
    """Size group "Infants" for wearables."""
    WearableSizeGroupJuniors = Schema(schema_storage["WearableSizeGroupJuniors"])
    """Size group "Juniors" for wearables."""
    WearableSizeGroupMaternity = Schema(schema_storage["WearableSizeGroupMaternity"])
    """Size group "Maternity" for wearables."""
    WearableSizeGroupMens = Schema(schema_storage["WearableSizeGroupMens"])
    """Size group "Mens" for wearables."""
    WearableSizeGroupMisses = Schema(schema_storage["WearableSizeGroupMisses"])
    """Size group "Misses" (also known as "Missy") for wearables."""
    WearableSizeGroupPetite = Schema(schema_storage["WearableSizeGroupPetite"])
    """Size group "Petite" for wearables."""
    WearableSizeGroupPlus = Schema(schema_storage["WearableSizeGroupPlus"])
    """Size group "Plus" for wearables."""
    WearableSizeGroupRegular = Schema(schema_storage["WearableSizeGroupRegular"])
    """Size group "Regular" for wearables."""
    WearableSizeGroupShort = Schema(schema_storage["WearableSizeGroupShort"])
    """Size group "Short" for wearables."""
    WearableSizeGroupTall = Schema(schema_storage["WearableSizeGroupTall"])
    """Size group "Tall" for wearables."""
    WearableSizeGroupWomens = Schema(schema_storage["WearableSizeGroupWomens"])
    """Size group "Womens" for wearables."""
    WearableSizeSystemAU = Schema(schema_storage["WearableSizeSystemAU"])
    """Australian size system for wearables."""
    WearableSizeSystemBR = Schema(schema_storage["WearableSizeSystemBR"])
    """Brazilian size system for wearables."""
    WearableSizeSystemCN = Schema(schema_storage["WearableSizeSystemCN"])
    """Chinese size system for wearables."""
    WearableSizeSystemContinental = Schema(
        schema_storage["WearableSizeSystemContinental"]
    )
    """Continental size system for wearables."""
    WearableSizeSystemDE = Schema(schema_storage["WearableSizeSystemDE"])
    """German size system for wearables."""
    WearableSizeSystemEN13402 = Schema(schema_storage["WearableSizeSystemEN13402"])
    """EN 13402 (joint European standard for size labelling of clothes)."""
    WearableSizeSystemEnumeration = Schema(
        schema_storage["WearableSizeSystemEnumeration"]
    )
    """Enumerates common size systems specific for wearable products."""
    WearableSizeSystemEurope = Schema(schema_storage["WearableSizeSystemEurope"])
    """European size system for wearables."""
    WearableSizeSystemFR = Schema(schema_storage["WearableSizeSystemFR"])
    """French size system for wearables."""
    WearableSizeSystemGS1 = Schema(schema_storage["WearableSizeSystemGS1"])
    """GS1 (formerly NRF) size system for wearables."""
    WearableSizeSystemIT = Schema(schema_storage["WearableSizeSystemIT"])
    """Italian size system for wearables."""
    WearableSizeSystemJP = Schema(schema_storage["WearableSizeSystemJP"])
    """Japanese size system for wearables."""
    WearableSizeSystemMX = Schema(schema_storage["WearableSizeSystemMX"])
    """Mexican size system for wearables."""
    WearableSizeSystemUK = Schema(schema_storage["WearableSizeSystemUK"])
    """United Kingdom size system for wearables."""
    WearableSizeSystemUS = Schema(schema_storage["WearableSizeSystemUS"])
    """United States size system for wearables."""
    WebAPI = Schema(schema_storage["WebAPI"])
    """An application programming interface accessible over Web/Internet
    technologies."""
    WebApplication = Schema(schema_storage["WebApplication"])
    """Web applications."""
    WebContent = Schema(schema_storage["WebContent"])
    """WebContent is a type representing all <a class="localLink"
    href="#sc.WebPage">WebPage</a>, <a class="localLink" href="#sc.WebSite">WebSite</a>
    and <a class="localLink" href="#sc.WebPageElement">WebPageElement</a> content.

    It is sometimes the case that detailed distinctions between Web pages, sites and
    their parts is not always important or obvious. The  <a class="localLink"
    href="#sc.WebContent">WebContent</a> type makes it easier to describe Web-
    addressable content without requiring such distinctions to always be stated. (The
    intent is that the existing types <a class="localLink"
    href="#sc.WebPage">WebPage</a>, <a class="localLink" href="#sc.WebSite">WebSite</a>
    and <a class="localLink" href="#sc.WebPageElement">WebPageElement</a> will
    eventually be declared as subtypes of <a class="localLink"
    href="#sc.WebContent">WebContent</a>).
    """
    WebPage = Schema(schema_storage["WebPage"])
    """A web page.

    Every web page is implicitly assumed to be declared to be of type WebPage, so the
    various properties about that webpage, such as <code>breadcrumb</code> may be used.
    We recommend explicit declaration if these properties are specified, but if they are
    found outside of an itemscope, they will be assumed to be about the page.
    """
    WebPageElement = Schema(schema_storage["WebPageElement"])
    """A web page element, like a table or an image."""
    WebSite = Schema(schema_storage["WebSite"])
    """A WebSite is a set of related web pages and other items typically served from a
    single web domain and accessible via URLs."""
    Wednesday = Schema(schema_storage["Wednesday"])
    """The day of the week between Tuesday and Thursday."""
    WesternConventional = Schema(schema_storage["WesternConventional"])
    """The conventional Western system of medicine, that aims to apply the best
    available evidence gained from the scientific method to clinical decision making.

    Also known as conventional or Western medicine.
    """
    Wholesale = Schema(schema_storage["Wholesale"])
    """The drug's cost represents the wholesale acquisition cost of the drug."""
    WholesaleStore = Schema(schema_storage["WholesaleStore"])
    """A wholesale store."""
    WinAction = Schema(schema_storage["WinAction"])
    """The act of achieving victory in a competitive activity."""
    Winery = Schema(schema_storage["Winery"])
    """A winery."""
    Withdrawn = Schema(schema_storage["Withdrawn"])
    """Withdrawn."""
    WorkBasedProgram = Schema(schema_storage["WorkBasedProgram"])
    """A program with both an educational and employment component.

    Typically based at a workplace and structured around work-based learning, with the
    aim of instilling competencies related to an occupation. WorkBasedProgram is used to
    distinguish programs such as apprenticeships from school, college or other classroom
    based educational programs.
    """
    WorkersUnion = Schema(schema_storage["WorkersUnion"])
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an
    organization that promotes the interests of its worker members by collectively
    bargaining with management, organizing, and political lobbying."""
    WriteAction = Schema(schema_storage["WriteAction"])
    """The act of authoring written creative content."""
    WritePermission = Schema(schema_storage["WritePermission"])
    """Permission to write or edit the document."""
    XPathType = Schema(schema_storage["XPathType"])
    """Text representing an XPath (typically but not necessarily version 1.0)."""
    XRay = Schema(schema_storage["XRay"])
    """X-ray imaging."""
    ZoneBoardingPolicy = Schema(schema_storage["ZoneBoardingPolicy"])
    """The airline boards by zones of the plane."""
    Zoo = Schema(schema_storage["Zoo"])
    """A zoo."""


del schema_storage
